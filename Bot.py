from telegram.ext import Updater, MessageHandler, Filters


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    REQUEST_KWARGS = {'proxy_url': 'socks5://207.97.174.134:1080'}
    updater = Updater(token='1178611560:AAGsJ0EbKPFc2yy7I1h7tJSbB647U9MB-Nc', use_context=True,
                      request_kwargs=REQUEST_KWARGS)

    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
