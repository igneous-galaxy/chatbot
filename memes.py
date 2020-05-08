import requests


def get_url():
    contents = requests.get('https://meme-api.herokuapp.com/gimme').json()
    url = contents['url']
    return url


def meme(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
