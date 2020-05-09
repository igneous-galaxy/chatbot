from Bot import *
from main_session import *


def cancel(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    if id in test_dict.keys():
        del test_dict[id]

    if id in talking_now.keys():
        del talking_now[id]

    if id in translate_dict.keys():
        del translate_dict[id]

    text = TEXT[user.mode]['cancel']

    update.message.reply_text(text)