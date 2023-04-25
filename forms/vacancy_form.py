from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class VacancyForm(FlaskForm):

    title = StringField('Название вакансии', validators=[DataRequired()])
    sphere = StringField('Сфера деятельности', validators=[DataRequired()])
    salary = IntegerField('Зарплата', validators=[DataRequired()])
    min_experience = IntegerField('Минимальный опыт работы', validators=[DataRequired()])
    description = TextAreaField('Описание вакансии', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
