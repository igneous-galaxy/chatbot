from Bot import *
from all_comands.talking.dialogue import which_response
from reader import TALKING
from main_session import session, talking_now


def talk(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()
    markup = ReplyKeyboardMarkup([['❌']])

    if id not in talking_now.keys():
        talking_now[id] = TALKING[update.message.text]

        update.message.reply_text(TEXT[user.mode][talking_now[id]], reply_markup=markup)
        return 1

    response = which_response(update.message.text, talking_now[id])
    update.message.reply_text(response, reply_markup=markup)

    return 1


def pick_up_topic(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    text = TEXT[user.mode]['talk']
    commands = COMMANDS[user.mode]['talk'] + ['❌']
    markup = ReplyKeyboardMarkup([commands], one_time_keyboard=True)

    update.message.reply_text(text, reply_markup=markup)

    return 1
