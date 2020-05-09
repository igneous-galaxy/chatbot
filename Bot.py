from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from reader import TOKEN, TEXT, COMMANDS
from data.users import User
from all_comands import memes, talk, lesson, recommend, test, translate, help, cancel, lang_change, start




def main():
    rec_handler = ConversationHandler(
        entry_points=[CommandHandler('recommend', recommend.recommend)],
        states={
            1: [MessageHandler(Filters.text(['фильм', 'книга', 'book', 'film']), recommend.get_rec)]
        },
        fallbacks=[MessageHandler(Filters.text(['❌']), cancel.cancel)],
        allow_reentry=True
    )

    test_handler = ConversationHandler(
        entry_points=[CommandHandler('test', test.test)],
        states={
            1: [MessageHandler(Filters.text & (~Filters.text(['❌'])), test.go_test)]
        },
        fallbacks=[MessageHandler(Filters.text(['❌']), cancel.cancel)],
        allow_reentry=True
    )

    translate_handler = ConversationHandler(
        entry_points=[CommandHandler('translate', translate.choose_tr_lang)],
        states={
            1: [MessageHandler(Filters.text(["ru -> en", "en -> ru"]), translate.get_tr_lang)],
            2: [MessageHandler(Filters.text & (~Filters.text(['❌'])), translate.translate)]
        },
        fallbacks=[MessageHandler(Filters.text(['❌']), cancel.cancel)],
        allow_reentry=True
    )

    lesson_handler = ConversationHandler(
        entry_points=[CommandHandler('lesson', lesson.lesson)],
        states={
            1: [MessageHandler(Filters.text & (~Filters.text(['❌'])), lesson.send_lesson)]
        },
        fallbacks=[MessageHandler(Filters.text(['❌']), cancel.cancel)],
        allow_reentry=True
    )

    talk_handler = ConversationHandler(
        entry_points=[CommandHandler('talk', talk.pick_up_topic)],
        states={
            1: [MessageHandler(Filters.text & (~Filters.text(['❌'])), talk.talk)]
        },
        fallbacks=[MessageHandler(Filters.text(['❌']), cancel.cancel)],
        allow_reentry=True
    )

    print('start')
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start.start))
    dp.add_handler(CommandHandler('en', lang_change.en))
    dp.add_handler(CommandHandler('ru', lang_change.ru))
    dp.add_handler(CommandHandler('help', help.help))
    dp.add_handler(CommandHandler('meme', memes.send_meme))

    dp.add_handler(rec_handler)
    dp.add_handler(test_handler)
    dp.add_handler(translate_handler)
    dp.add_handler(lesson_handler)
    dp.add_handler(talk_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
