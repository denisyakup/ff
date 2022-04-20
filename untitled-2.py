from flask import Flask, url_for, render_template
from flask import request 
import requests
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def imagee():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def bootstrap():
    return 'И на Марсе будут яблони цвести!'

#@app.route('promotion')
#def prom():
#    return

@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                  <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1> Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}">
                    <h3 style="color:#ff0000; background-color:#ffc0cb">Человечество вырастает из детства</h3>
                    <h4 style="color:#ffc0b; background-color:#0000ff">Человечеству мала одна планета</h4>
                    <h5 style="color:#50c878; background-color:#009900">Мы сделаем обитаемыми безжизненные пока планеты</h5>
                    <h6  style="color:#ff0000; background-color:#ffc0cb">И начнем с Марса!</h6>
                    <h7 style='color:#666600; background-color:#ffff00'>Присоединяйся</h7>
                  </body>
                </html>"""

@app.route('/choice/<planet_name>')
def choice(planet_name):
    planet = planet_name
    if planet == 'Земля':
        return render_template('earth.html', planet=planet_name)        
    elif planet == 'Марс':
        return render_template('mars.html', planet=planet_name)
    elif planet == 'Меркурий':
        return render_template('mercury.html', planet=planet_name)
    elif planet == 'Венера':
        return render_template('venus.html', planet=planet_name)        
        
    elif planet == 'Юпитер':
        return render_template('jupiter.html', planet=planet_name)       
        
    elif planet == 'Уран':
        return render_template('uranus.html', planet=planet_name)        
        
    elif planet == 'Нептун':
        return render_template('neptune.html', planet=planet_name)       
    elif planet == 'Сатурн':
        return render_template('saturn.html', planet=planet_name)                       
    elif planet == 'Плутон':
        return render_template('pluton.html', planet=planet_name)       

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):        
    return render_template('res.html', nick=nickname, lvl=level, rate=rating)




@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return render_template('image.html')
    elif request.method == 'POST':
        #ff = request.files['file']
        #p = requests.get(request.files['file'])
        f = request.files['file']
        p = f.read()
        #print(p.content)
        print(request.files['file'].read())
        out = open("static/img/ava.jpg", "wb")
        out.write(p)
        out.close()
        return render_template('image.html')

@app.route('/distribution')
def distribution():
    return render_template('distribution.html')

@app.route('/table/<male>/<int:age>')
def table(male, age):
    return render_template('table.html', male=male, age=age)

@app.route('/member')
def member():
    with open("templates/members.json", "r") as read_file:
        data = json.load(read_file)
    names = []
    for i in data:
        names.append(i)
    name = names[random.randint(0, 2)]
    jobs = data[name]
    job = ', '.join(map(str, jobs)) 
    file1 = ['img/ava_1.png', 'img/ava_2.png', 'img/ava_3.png']
    return render_template('member.html', name=names, jobs=job, file=file1)
    

 
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')