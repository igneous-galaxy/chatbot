import sqlalchemy
from .db_session import SqlAlchemyBase


class Book(SqlAlchemyBase):
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    level = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    plot_ru = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    plot_en = sqlalchemy.Column(sqlalchemy.String, nullable=True)