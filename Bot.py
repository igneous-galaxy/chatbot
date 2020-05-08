from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from reader import TOKEN, TEXT, COMMANDS, read_json
from data import db_session
from data.users import User
from data.films import Film
from data.books import Book
from random import randint
from test_class import Test
import requests


db_session.global_init("db/global.sqlite")
session = db_session.create_session()
test_dict = {}
translate_dict = {}


def start(update, context):
    users = list(map(lambda x: x.id, session.query(User).all()))
    id = update.message.from_user.id

    if id not in users:
        new = User(id=id, mode='en')
        session.add(new)
        session.commit()
    else:
        new = session.query(User).filter(User.id == id).first()

    text = TEXT[new.mode]['start']

    update.message.reply_text(text)


def choose_tr_lang(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    markup = ReplyKeyboardMarkup([COMMANDS[user.mode]['translate'] + ['❌']], one_time_keyboard=True)

    update.message.reply_text(TEXT[user.mode]['translate'][0], reply_markup=markup)

    return 1


def get_tr_lang(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    test_dict[id] = update.message.text

    text = TEXT[user.mode]['translate'][1]
    markup = ReplyKeyboardMarkup([['❌']], one_time_keyboard=True)

    update.message.reply_text(text, reply_markup=markup)

    return 2


def translate(update, context):
    api_key = 'trnsl.1.1.20200505T115405Z.e81ba43b2a560407.b24350720bd63bd44082ff3421f476145d467343'
    id = update.message.from_user.id
    lang = 'ru-en' if test_dict[id] == 'ru -> en' else 'en-ru'

    response = requests.get(f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={api_key}&lang={lang}&text={update.message.text}').json()

    update.message.reply_text(response['text'][0])

    return 2


def help(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    text = TEXT[user.mode]['help']

    update.message.reply_text(text)


def recommend(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    markup = ReplyKeyboardMarkup([COMMANDS[user.mode]['rec']], one_time_keyboard=True)

    text = TEXT[user.mode]['rec'][0]

    update.message.reply_text(text, reply_markup=markup)

    return 1


def get_rec(update, context):
    print(1)
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    kind = update.message.text

    if kind == 'фильм' or kind == 'film':
        length = session.query(Film).count()
        rand = randint(1, length)

        rec = user.rec_films
        res = session.query(Film).filter(Film.id == rand).first()

        if rec is None:
            rec = ''

        while str(rand) in rec.split() or res is None:
            rand = randint(1, length)
            res = session.query(Film).filter(Film.id == rand).first()

        user.rec_films = rec + f' {str(rand)}'

        res = f'🟠{res.name}\n\n🔸{res.plot_ru}' \
            if user.mode == 'ru' else f'🟠{res.name}\n\n🔸{res.plot_en}'

    elif kind == 'книга' or kind == 'book':

        length = session.query(Book).count()
        rand = randint(1, length)

        rec = user.rec_books

        res = session.query(Book).filter(Book.id == rand).first()

        if rec is None:
            rec = ''

        while str(rand) in rec.split() or res is None:
            rand = randint(1, length)
            res = session.query(Book).filter(Book.id == rand).first()

        user.rec_books = rec + f' {str(rand)}'

        res = f'🟠{res.author} - {res.name}\n\n🔸{res.plot_ru}' \
            if user.mode == 'ru' else \
            f'🟠{res.author} - {res.name}\n\n🔸{res.plot_en}'

    text = TEXT[user.mode]['rec'][1]
    session.commit()

    update.message.reply_text(text + res, reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def test(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    text = TEXT[user.mode]['test'][0]
    commands = COMMANDS[user.mode]['test'] + ['❌']
    markup = ReplyKeyboardMarkup([commands], one_time_keyboard=True)

    update.message.reply_text(text, reply_markup=markup)

    return 1


def go_test(update, context):
    id = update.message.from_user.id

    if id not in test_dict.keys():
        path = 'tests/' + update.message.text + '.json'
        test_dict[id] = Test(read_json(path))
    else:
        test_dict[id].check_it(update.message.text)

    current = test_dict[id]
    text = current.ask_next()
    print(text)

    if text['count'] == 10:
        count = current.get_result()

        user = session.query(User).filter(User.id == id).first()
        res = TEXT[user.mode]['test']

        update.message.reply_text(f'{res[1]} {count}/10\n{res[2]}', reply_markup=ReplyKeyboardRemove())
        del test_dict[id]

        return ConversationHandler.END
    elif text['markup'] is not None:
        markup = ReplyKeyboardMarkup([text['markup'] + ['❌']], one_time_keyboard=True)
        update.message.reply_text(text['text'], reply_markup=markup)
    else:
        markup = ReplyKeyboardMarkup([['❌']], one_time_keyboard=True)
        update.message.reply_text(text['text'], reply_markup=markup)

    return 1



def lesson(update, context):
    pass


def talk(update, context):
    pass


def ru(update, context):
    id = update.message.from_user.id

    user = session.query(User).filter(User.id == id).first()
    user.mode = 'ru'
    session.commit()

    update.message.reply_text('Готово!')


def en(update, context):
    id = update.message.from_user.id

    user = session.query(User).filter(User.id == id).first()
    user.mode = 'en'
    session.commit()

    update.message.reply_text('Done!')


def cancel(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    if id in test_dict.keys():
        del test_dict[id]

    text = TEXT[user.mode]['cancel']

    update.message.reply_text(text)


def main():
    rec_handler = ConversationHandler(
        entry_points=[CommandHandler('recommend', recommend)],
        states={
            1: [MessageHandler(Filters.text(['фильм', 'книга', 'book', 'film']), get_rec)]
        },
        fallbacks=[MessageHandler(Filters.text(['❌']), cancel)],
        allow_reentry=True
    )

    test_handler = ConversationHandler(
        entry_points=[CommandHandler('test', test)],
        states={
            1: [MessageHandler(Filters.text & (~Filters.text(['❌'])), go_test)]
        },
        fallbacks=[MessageHandler(Filters.text(['❌']), cancel)],
        allow_reentry=True
    )

    translate_handler = ConversationHandler(
        entry_points=[CommandHandler('translate', choose_tr_lang)],
        states={
            1: [MessageHandler(Filters.text(["ru -> en", "en -> ru"]), get_tr_lang)],
            2: [MessageHandler(Filters.text & (~Filters.text(['❌'])), translate)]
        },
        fallbacks=[MessageHandler(Filters.text(['❌']), cancel)],
        allow_reentry=True
    )


    print('start')
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('en', en))
    dp.add_handler(CommandHandler('ru', ru))
    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(rec_handler)
    dp.add_handler(test_handler)
    dp.add_handler(translate_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
