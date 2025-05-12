import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Basket(SqlAlchemyBase):
    __tablename__ = 'basket'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    products_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    quantity = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    user = orm.relationship('User')
