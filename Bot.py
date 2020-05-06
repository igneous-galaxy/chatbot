from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup
from reader import TOKEN, TEXT
from data import db_session
from data.users import User


db_session.global_init("db/global.sqlite")
session = db_session.create_session()


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


def translate(update, context):
    pass


def help(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    text = TEXT[user.mode]['help']

    update.message.reply_text(text)


def recommend(update, context):
    pass


def test(update, context):
    pass


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


def main():

    # conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler('start', start)],
    #     states={
    #         1: [MessageHandler(Filters.text & (~Filters.command), go),
    #             CommandHandler('go', go)]
    #     },
    #     fallbacks=[CommandHandler('stop', stop)]
    # )


    print('start')
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('en', en))
    dp.add_handler(CommandHandler('ru', ru))
    dp.add_handler(CommandHandler('help', help))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
