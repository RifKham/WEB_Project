import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Product(SqlAlchemyBase):
    __tablename__ = 'product'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    rating = sqlalchemy.Column(sqlalchemy.Float, default=0.00)
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
    wtype = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    weaponry = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    building_material = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tool = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    used = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User', back_populates='product')
    comments = orm.relationship('Comment', back_populates='product')
