from flask import Flask, render_template, url_for, request, redirect
from loginform import LoginForm, Protection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


data = {}


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())


@app.route('/list_prof/<lst>')
def list_prof(lst):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_prof.html', list=lst, professions=professions)


@app.route('/answer')
def answer():
    global data
    keys_1 = list(data.keys())[0:-2]
    keys_1.remove('email')
    dict_ = {}
    keys_2 = ['Фамилия', 'Имя', 'Образование', 'Профессия', 'Пол', 'Мотивация', 'Готовы ли вы остаться на Марсе?']
    for i in range(len(keys_1)):
        dict_[keys_2[i]] = data[keys_1[i]]
    lst = dict_.keys()
    return render_template('answer.html', list=lst, dict=dict_)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global data
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        return redirect('/answer')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/protection', methods=['GET', 'POST'])
def protection():
    global data
    form = Protection()
    if form.validate_on_submit():
        data = form.data
        return redirect('/answer')
    return render_template('protection.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
