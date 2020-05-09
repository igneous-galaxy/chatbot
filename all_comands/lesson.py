from Bot import *
from reader import LESSONS
from main_session import session


def lesson(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    commands = ReplyKeyboardMarkup([COMMANDS[user.mode]['lessons'] + ['❌']], one_time_keyboard=True)

    text = TEXT[user.mode]['lessons'][0]

    update.message.reply_text(text, reply_markup=commands)

    return 1


def send_lesson(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    update.message.reply_photo(photo=open(f'all_comands/lessons/{LESSONS[update.message.text]}', 'rb'))
    update.message.reply_text(TEXT[user.mode]['lessons'][1])

    return 1