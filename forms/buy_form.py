from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class PurchaseForm(FlaskForm):
    product_id = IntegerField('ID товара', validators=[DataRequired(), NumberRange(min=1)])
    quantity = IntegerField('Количество', validators=[DataRequired(), NumberRange(min=1, max=100)])

    submit = SubmitField('Оформить заказ')
