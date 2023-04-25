import logging

from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session
from data.resumes import Resume
from data.users import User
from data.vacancies import Vacancy
from forms.login_user_form import LoginForm
from forms.register_user_form import RegisterForm
from forms.resume_form import ResumeForm
from forms.vacancy_form import VacancyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    logging.basicConfig(level=logging.INFO, filename='info.txt')
    db_session.global_init("db/blogs.db")
    app.run(debug=True, host='127.0.0.1', port=5000)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    data = db_sess.query(Vacancy).all()
    return render_template('index.html', title='Jooble', data=data)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_required
@app.route('/employer/<int:id>')
def employer(id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id).first()
    user.is_employer = True
    db_sess.commit()
    return redirect(f'/personal_account/{id}')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login_user.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login_user.html', title='Авторизация', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register_user.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register_user.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register_user.html', title='Регистрация', form=form)


@app.route('/vacancy/<int:id>')
def vacancy_page(id):
    logging.warning('a')
    db_sess = db_session.create_session()
    item = db_sess.query(Vacancy).filter(Vacancy.id == id).first()
    return render_template('vacancy.html', vacancy=item)


@login_required
@app.route('/personal_account/<int:id>')
def personal_account(id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id).first()
    logging.warning(user)
    return render_template('personal_account.html', user=user)


@login_required
@app.route('/resume/<int:id>', methods=['GET', 'POST'])
def resume(id):
    form = ResumeForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        resume = db_sess.query(Resume).filter(Resume.owner_id == id).first()
        resume.text = form.resume.data
        resume.sphere = form.sphere.data
        resume.education = form.education.data
        resume.experience_time = form.experience_time.data
        db_sess.commit()
        return redirect(f'/personal_account/{id}')
    db_sess = db_session.create_session()
    resume = db_sess.query(Resume).filter(Resume.owner_id == id).first()
    if not resume:
        resume = Resume()
        resume.owner_id = id
        db_sess.add(resume)
        user = db_sess.query(User).filter(User.id == id).first()
        user.resume_id = resume.id
        db_sess.commit()
    # logging.warning(form.resume)
    # logging.warning(user.resume)
    return render_template('resume.html', title='Резюме', form=form, resume=resume)


@app.route('/resumes', methods=['GET'])
def all_resumes():
    db_sess = db_session.create_session()
    data = db_sess.query(Resume).all()
    return render_template('all_resumes.html', title='Все резюме', data=data)


@app.route('/employer_vacancies/<int:id>')
def employer_vacancies(id):
    db_sess = db_session.create_session()
    vacancies = db_sess.query(Vacancy).filter(Vacancy.owner == id)
    return render_template('employer_vacancies.html', vacancies=vacancies, id=id)


@login_required
@app.route('/make_vacancy/<int:id>', methods=['GET', 'POST'])
def make_vacancy(id):
    form = VacancyForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        vacancy = Vacancy(
            title=form.title.data,
            description=form.description.data,
            owner=id
        )
        db_sess.add(vacancy)
        db_sess.commit()
        return redirect(f'/personal_account/{id}')
    return render_template('vacancy_make.html', title='Резюме', form=form, id=id)


if __name__ == '__main__':
    main()
