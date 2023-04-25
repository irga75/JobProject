from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField, SelectField
from wtforms.validators import DataRequired


class VacancyForm(FlaskForm):

    title = StringField('Название вакансии', validators=[DataRequired()])
    sphere = SelectField('Сфера деятельности', choices=['Информационная', 'Экономика', 'Производство'])
    salary = IntegerField('Зарплата', validators=[DataRequired()])
    min_experience = IntegerField('Минимальный опыт работы', validators=[DataRequired()])
    description = TextAreaField('Описание вакансии', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
