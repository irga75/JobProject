from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class VacancyForm(FlaskForm):

    title = StringField('Название вакансии', validators=[DataRequired()])
    description = TextAreaField('Описание вакансии', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
