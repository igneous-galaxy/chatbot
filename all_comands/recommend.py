from Bot import *
from random import randint
from data.films import Film
from data.books import Book
from main_session import session


def recommend(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    markup = ReplyKeyboardMarkup([COMMANDS[user.mode]['rec']], one_time_keyboard=True)

    text = TEXT[user.mode]['rec'][0]

    update.message.reply_text(text, reply_markup=markup)

    return 1


def get_rec(update, context):
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