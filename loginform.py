from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    education = SelectField('Ваше образование', choices=[('общее', 'общее'),
                                                         ('среднее', 'среднее'), ('высшее', 'высшее')])
    radio_prof = RadioField('Ваша специальность', choices=['инженер-исследователь', 'врач', 'климатолог',
                                                           'пилот', 'строитель', 'экзобиолог', 'киберинженер'])
    radio_sex = RadioField('Ваш пол', choices=['Мужской', 'Женский'])
    comment = TextAreaField('Почему вы хотите принять участие в миссии?')
    remember_me = BooleanField('Готовы ли вы остаться на Марсе?')
    submit = SubmitField('Войти')