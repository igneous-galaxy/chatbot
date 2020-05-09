from Bot import *
from data.users import User
from main_session import session


def start(update, context):
    print('go')
    print(session)
    users = list(map(lambda x: x.id, session.query(User).all()))
    id = update.message.from_user.id
    print('go 1')

    if id not in users:
        new = User(id=id, mode='en')
        session.add(new)
        session.commit()
    else:
        new = session.query(User).filter(User.id == id).first()

    text = TEXT[new.mode]['start']

    update.message.reply_text(text)
