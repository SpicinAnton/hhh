from flask import Flask, url_for

app = Flask(__name__)


@app.route('/promotion_image')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас Марс<h1>
                    <img src="/static/img/mars22.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <h2>Человечество вырастает из детства.</h2>
                    <h3>Человечеству мала одна планета.<h3>
                     <h4>Мы сделаем обитаемыми безжизненные пока планеты.</h4>
                     <h5>И начнем с Марса!</h5>
                     <h6>Присоединяйся!</h6>
                  </body>                 
                </html>"""


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
