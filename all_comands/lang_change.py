from Bot import *
from main_session import session


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