import datetime

import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from data.db_session import SqlAlchemyBase


class Resume(SqlAlchemyBase, UserMixin):
    """Вакансии - работы от работодателей"""
    __tablename__ = 'resumes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    text = sqlalchemy.Column(sqlalchemy.String)
    owner_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    sphere = sqlalchemy.Column(sqlalchemy.String)
    experience_time = sqlalchemy.Column(sqlalchemy.Integer)
    education = sqlalchemy.Column(sqlalchemy.String)

    owner = orm.relationship('User')
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default=datetime.datetime.now)

    def __repr__(self):
        return f'<Resume> {self.id} {self.owner}'
