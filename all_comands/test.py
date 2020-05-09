from Bot import *
from reader import read_json
from all_comands.test_class import Test
from main_session import session, test_dict


def test(update, context):
    id = update.message.from_user.id
    user = session.query(User).filter(User.id == id).first()

    text = TEXT[user.mode]['test'][0]
    commands = COMMANDS[user.mode]['test'] + ['❌']
    markup = ReplyKeyboardMarkup([commands], one_time_keyboard=True)

    update.message.reply_text(text, reply_markup=markup)

    return 1


def go_test(update, context):
    id = update.message.from_user.id

    if id not in test_dict.keys():
        path = 'all_comands/tests/' + update.message.text + '.json'
        test_dict[id] = Test(read_json(path))
    else:
        test_dict[id].check_it(update.message.text)

    current = test_dict[id]
    text = current.ask_next()

    if text['count'] == 10:
        count = current.get_result()

        user = session.query(User).filter(User.id == id).first()
        res = TEXT[user.mode]['test']

        update.message.reply_text(f'{res[1]} {count}/10\n{res[2]}', reply_markup=ReplyKeyboardRemove())
        del test_dict[id]

        return ConversationHandler.END
    elif text['markup'] is not None:
        markup = ReplyKeyboardMarkup([text['markup'] + ['❌']], one_time_keyboard=True)
        update.message.reply_text(text['text'], reply_markup=markup)
    else:
        markup = ReplyKeyboardMarkup([['❌']], one_time_keyboard=True)
        update.message.reply_text(text['text'], reply_markup=markup)

    return 1