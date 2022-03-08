from flask import Flask, render_template, url_for, request, redirect
import datetime
from data.jobs import Jobs
from loginform import LoginForm, Protection, LoadPhoto, RegisterForm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register',  methods=['GET', 'POST'])
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


if __name__ == '__main__':
    db_session.global_init('db/users.db')
    session = db_session.create_session()
    app.run(port=8080, host='127.0.0.1')


