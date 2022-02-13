from flask import Flask, url_for

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')