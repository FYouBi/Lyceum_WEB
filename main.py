import flask
from flask import Flask, render_template, url_for, request, redirect, jsonify
import datetime
from data.jobs import Jobs
from forms import LoginForm, Protection, LoadPhoto, RegisterForm
from data import db_session
from data.users import User
from requests import get

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/<job_id>')
def job(job_id):
    try:
        job_id = int(job_id)
    except:
        return jsonify({'error': 'Incorrect request'})
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if jobs:
        return jsonify(
            {
                'jobs':
                    [jobs.to_dict(only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader'))]
            }
        )
    return jsonify({'error': f'Not found job with id {job_id}'})


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader'))
                 for item in news]
        }
    )


@blueprint.route('/api/new_job', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'job', 'work_size', 'collaborators', 'is_finished', 'team_leader']):
        return jsonify({'error': 'Bad request'})
    a = []
    for i in session.query(Jobs).filter(Jobs.id == request.json['id']):
        a.append(i)
    if a:
        return jsonify({'error': f'Id already exists'})
    db_sess = db_session.create_session()
    job = Jobs(
        id=request.json['id'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
        team_leader=request.json['team_leader']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        print(data)
        new_user = User(name=data['name'], surname=data['surname'],
                        age=int(data['age']), position=data['position'], hashed_password=data['password'],
                        speciality=data['speciality'], address=data['address'], email=data['login_email'])
        session.add(new_user)
        session.commit()
        return 'ok'
    return render_template('register.html', title='Авторизация', form=form)


@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        email, password = form.data['email'], form.data['password']
        for user in db_sess.query(User).all():
            if user.email == email:
                if user.hashed_password == password:
                    return render_template('base.html')
                return render_template('authorization.html', title='Authorization', message='Неверный пароль',
                                       form=form, list=[form.email, form.password])
        return render_template('authorization.html', title='Authorization', message='Неверный логин',
                               form=form, list=[form.email, form.password])
    return render_template('authorization.html', title='Authorization', message='',
                           form=form, list=[form.email, form.password])


if __name__ == '__main__':
    db_session.global_init('db/users.db')
    session = db_session.create_session()
    app.register_blueprint(blueprint)
    app.run(port=5000, host='127.0.0.1')