from werkzeug.security import generate_password_hash

from data import db_session
from data.users import User


def create_admin_user():
    user = User()
    user.name = "Админ"
    user.email = "admin@admin.admin"
    user.hashed_password = generate_password_hash("123")
    user.age = 10000
    user.city = "Канаш"
    user.role = "a"
    user.balance = 123456789
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
