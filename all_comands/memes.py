from Bot import *
import requests
from main_session import session


def get_url():
    contents = requests.get('https://meme-api.herokuapp.com/gimme').json()
    url = contents['url']
    return url


def send_meme(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    update.message.reply_photo(photo=memes.get_url())
    update.message.reply_text(TEXT[user.mode]['memes'])
