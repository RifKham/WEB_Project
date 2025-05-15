from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, TextAreaField
from wtforms import SubmitField, FloatField, BooleanField
from wtforms.fields.choices import SelectField, RadioField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    content = TextAreaField("Описание")
    price = FloatField("Цена в ₽", validators=[DataRequired()])
    quantity = IntegerField("Количество", validators=[DataRequired()])
    submit = SubmitField('Применить')
    wtype = RadioField('Чем оно является?', choices=[('stick', 'Палка'), ('wood_work', 'Изделие из дерева'),
                                                     ('bark', 'Кора'), ('wood', 'Древесина')],
                       validators=[DataRequired()])
    weaponry = SelectField('Оружие/похоже на оружие', choices=[('no_w', 'Не оружие/не похоже на оружие'),
                                                               ('sword', 'Похоже на меч'), ('bow', 'Лук'),
                                                               ('gun', 'Похоже на огнестрел'),
                                                               ('slingshot', 'Рогатка'), ('shield', 'Щит')],
                           default=('no_w', 'Не оружие/не похоже на оружие'),
                           validators=[DataRequired()])
    building_material = SelectField("Стройматериал", choices=[('no_bm', 'Не стройматериал'), ("plank", "Доски"),
                                                              ("column", "Колонна")],
                                    default=('no_bm', 'Не стройматериал'), validators=[DataRequired()])
    tool = BooleanField("Инструмент")
    used = BooleanField('Б/У')
    image = FileField('Изображение')
