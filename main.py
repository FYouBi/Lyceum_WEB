from flask import Flask, render_template, url_for, request, redirect
import datetime
from data.jobs import Jobs
from loginform import LoginForm, Protection, LoadPhoto
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


if __name__ == '__main__':
    # app.run(port=8080, host='127.0.0.1')
    db_session.global_init('db/' + input())
    session = db_session.create_session()

    for user in session.query(User):
        print(user)


