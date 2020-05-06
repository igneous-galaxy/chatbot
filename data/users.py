import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True)
    recomendations = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tests = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    mode = sqlalchemy.Column(sqlalchemy.String)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)