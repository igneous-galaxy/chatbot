from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from dialogue import response


def echo(update, context):
    update.message.reply_text(response(update.message.text))


def start(update, context):
    update.message.reply_text("Hi! I\'m Daniel! I\'ll help you with your english!")


def main():
    REQUEST_KWARGS = {'proxy_url': 'socks5://207.97.174.134:1080'}
    updater = Updater(token=TOKEN, use_context=True,
                      request_kwargs=REQUEST_KWARGS)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
