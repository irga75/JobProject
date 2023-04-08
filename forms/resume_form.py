from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class ResumeForm(FlaskForm):
    resume = TextAreaField('Моё резюме')
    submit = SubmitField('Сохранить')
