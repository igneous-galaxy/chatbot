from Bot import *
import requests
from reader import API_KEY
from main_session import session, translate_dict


def choose_tr_lang(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    markup = ReplyKeyboardMarkup([COMMANDS[user.mode]['translate'] + ['❌']], one_time_keyboard=True)

    update.message.reply_text(TEXT[user.mode]['translate'][0], reply_markup=markup)

    return 1


def get_tr_lang(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    translate_dict[id] = update.message.text

    text = TEXT[user.mode]['translate'][1]
    markup = ReplyKeyboardMarkup([['❌']], one_time_keyboard=True)

    update.message.reply_text(text, reply_markup=markup)

    return 2


def translate(update, context):
    id = update.message.from_user.id
    lang = 'ru-en' if translate_dict[id] == 'ru -> en' else 'en-ru'

    response = requests.get(f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={API_KEY}&lang={lang}&text={update.message.text}').json()

    update.message.reply_text(response['text'][0])

    return 2