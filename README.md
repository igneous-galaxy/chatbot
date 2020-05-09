# "Oh, Sir!" chatbot

Telegram chatbot that helps you learn English. It can send you memes from Reddit, and test you, talk with you, and educate you.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project.

### Prerequisites

What things you need to install the software and how to install them

```
pip install python-telegram-bot
pip install sklearn
pip install nltk
pip install requests
pip install PySocks
pip install sqlalchemy
pip install wheel
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
```

### Running

Run Bot.py

## Deployment

Get TOKEN from GodFather
Write it in settings.ini
```
[Bot]
token=YOUR_TOKEN
```
You might need a proxy
```
REQUEST_KWARGS = {'proxy_url': 'socks5://166.62.43.174:31178'}  # REQUEST_KWARGS = {'proxy_url': 'protocol://ip:port'}
updater = Updater(TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
```

## Authors

* **Елизавета Вольных** - [EV0320](https://github.com/EV0320)
* **Галина Игнатова** - [igalaxy-git](https://github.com/igalaxy-git)

See also the list of [contributors](https://github.com/igalaxy-git/chatbot/contributors) who participated in this project.

