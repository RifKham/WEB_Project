from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class PurchaseForm(FlaskForm):
    quantity = StringField('Количество', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Добавить в корзину')
