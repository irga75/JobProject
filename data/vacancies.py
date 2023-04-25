import datetime

import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from data.db_session import SqlAlchemyBase


class Vacancy(SqlAlchemyBase, UserMixin):
    """Вакансии - работы от работодателей"""
    __tablename__ = 'vacancies'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    sphere = sqlalchemy.Column(sqlalchemy.String)
    salary = sqlalchemy.Column(sqlalchemy.Integer)
    min_experience = sqlalchemy.Column(sqlalchemy.Integer)
    owner = sqlalchemy.Column(sqlalchemy.Integer)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default=datetime.datetime.now)

    def __repr__(self):
        return f'<Vacancy> {self.id} {self.title} {self.owner}'
