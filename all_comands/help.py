from Bot import *
from main_session import session


def help(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    text = TEXT[user.mode]['help']
    update.message.reply_text(text)