from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, SelectField, IntegerField
from wtforms.validators import DataRequired


class ResumeForm(FlaskForm):
    resume = TextAreaField('Моё резюме')
    sphere = SelectField('Сфера деятельности', choices=['Информационная', 'Экономика', 'Производство'])
    experience_time = IntegerField('Стаж работы')
    education = SelectField('Уровень образования',
                            choices=['Основное общее образование',
                                     'Среднее общее образование',
                                     'Начальное профессиональное образование',
                                     'Среднее профессиональное образование',
                                     'Высшее профессиональное образование'])
    submit = SubmitField('Сохранить')
