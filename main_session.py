from data import db_session

db_session.global_init("db/global.sqlite")
session = db_session.create_session()

test_dict = {}
translate_dict = {}
talking_now = {}