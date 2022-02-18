from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def countdown():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса<h1/>
                  </body>
                </html>"""


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    spisok = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(spisok)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!<h1/>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но нет">
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title></title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но нет">
                    <div class="alert alert-dark" role="alert">
                      Мне
                    </div>
                    <div class="alert alert-success" role="alert">
                      Лень
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Писать
                    </div>
                    <div class="alert alert-orange" role="alert">
                      Все
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Это
                    </div>
                  </body>
                </html>'''


@app.route('/form', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Form</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию">
                                    <div class="form-group">
                                        <h1><h1/>
                                    </div>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Общее</option>
                                          <option>Профессиональное</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="radio">Какая у вас профессия</label>
                                        <br/>
                                        <input type="radio" id="contactChoice1" name="contact" value="инженер-исследователь" checked>
                                        <label for="contactChoice1">инженер-исследователь</label>
                                        <br/>
                                        <input type="radio" id="contactChoice2" name="contact" value="пилот">
                                        <label for="contactChoice2">пилот</label>
                                        <br/>
                                        <input type="radio" id="contactChoice3" name="contact" value="строитель">
                                        <label for="contactChoice3">строитель</label>
                                        <br/>
                                        <input type="radio" id="contactChoice3" name="contact" value="экзобиолог">
                                        <label for="contactChoice3">экзобиолог</label>
                                        <br/>
                                        <input type="radio" id="contactChoice3" name="contact" value="врач">
                                        <label for="contactChoice3">врач</label>
                                        <br/>
                                        <input type="radio" id="contactChoice3" name="contact" value="климатолог">
                                        <label for="contactChoice3">климатолог</label>
                                        <br/>
                                        <input type="radio" id="contactChoice3" name="contact" value="киберинженер">
                                        <label for="contactChoice3">киберинженер</label>
                                     </div>
                                    <br/>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br/>
                                    <div class="form-group">
                                        <label for="form-check">Готовы ли вы остаться на Марсе?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" id="yes" value="yes">
                                          <label class="form-check-label" for="yes">
                                            Да
                                          </label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return choice('Меркурий')


@app.route('/choice/<planet_name>')
def choice(planet_name):
    first = ''
    second = ''
    third = ''
    fourth = ''
    if planet_name == 'Меркурий':
        first = 'Это самая'
        second = 'близкая'
        third = 'планета'
        fourth = 'к солнцу'
    if planet_name == 'Венера':
        first = 'Это планета.'
        second = 'не знаю что'
        third = 'еще'
        fourth = 'сказать'
    if planet_name == 'Земля':
        first = 'Ты'
        second = 'на'
        third = 'ней'
        fourth = 'живешь'
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title></title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-dark" role="alert">
                          {first}
                        </div>
                        <div class="alert alert-success" role="alert">
                          {second}
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          {third}
                        </div>
                        <div class="alert alert-orange" role="alert">
                          {fourth}
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title></title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <div>
                          Предендент на участие в миссии {nickname}
                        </div>
                        <div class="alert alert-success" role="alert">
                          Поздравляем! Ваш рейтинг после {level} этапа отбора
                        </div>
                        <div>
                          составляет: {rating}
                        </div>
                        <div class="alert alert-orange" role="alert">
                          Желаем удачи
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')