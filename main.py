from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session
from flask import Flask, render_template, redirect, abort, request

from data.product import Product
from data.users import User
from forms.balance_form import BalanceForm
from forms.login_form import LoginForm
from forms.products import ProductForm
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/products.sqlite")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    product = db_sess.query(Product)
    if "AnonymousUserMixin" not in str(current_user):
        return render_template("index.html", product=product, url="/profile", name_b=current_user.name)
    return render_template("index.html", product=product)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/profile")
@login_required
def profile():
    db_sess = db_session.create_session()
    product = db_sess.query(Product)
    return render_template("profile.html", product=product, url="/", name_b="Вернуться на главную")


@app.route("/balance", methods=["GET", "POST"])
@login_required
def balance():
    form = BalanceForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        current_user.balance += form.balance.data
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect("/")
    return render_template("balance.html", form=form)


@app.route('/products', methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        product = Product()
        product.title = form.title.data
        product.content = form.content.data
        product.price = form.price.data
        product.wtype = form.wtype.data
        product.weaponry = form.weaponry.data
        product.building_material = form.building_material.data
        product.tool = form.tool.data
        product.used = form.used.data

        current_user.product.append(product)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/profile')
    return render_template('product.html', title='Добавление новости',
                           form=form)


@app.route('/products/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    form = ProductForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        product = db_sess.query(Product).filter(Product.id == id,
                                                Product.user == current_user
                                                ).first()
        if product:
            form.title.data = product.title
            form.content.data = product.content
            form.price.data = product.price
            form.wtype.data = product.wtype
            form.weaponry.data = product.weaponry
            form.building_material.data = product.building_material
            form.tool.data = product.tool
            form.used.data = product.used

        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        product = db_sess.query(Product).filter(Product.id == id,
                                                Product.user == current_user
                                                ).first()
        if product:
            product.title = form.title.data
            product.content = form.content.data
            product.price = form.price.data
            product.wtype = form.wtype.data
            product.weaponry = form.weaponry.data
            product.building_material = form.building_material.data
            product.tool = form.tool.data
            product.used = form.used.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('product.html',
                           title='Редактирование товара',
                           form=form
                           )


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
