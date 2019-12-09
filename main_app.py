#!usr/bin/env python3
# flask run --host=0.0.0.0

from flask import Flask
from flask import render_template, jsonify
from flask import request, flash, redirect, Config
#import routes
from forms import LoginForm
from redis_p import *
#from routes import *

#uname="innute9"

app=Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#import routes

@app.route('/')
def intra_dat_fn():
    return 'hello Ruth'


@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/void')
def void_page():
    return render_template('void.html')


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/rend/')
@app.route('/rend/<name>')
def rend_page(name=None):
    return render_template('rend.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.is_submitted():
        name=form.username.data
        password=form.password.data
        #result=request.form
        #flash('Login requested for user {}, remember_me={}'.format(
        #    form.username.data, form.remember_me.data))
        return render_template('upload.html', name=name, password=password)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    data=None
    if request.method == "POST":
        #data=request.json['data']
        data=request.form['user']
        if data:
           #print(data)
           return jsonify({'data': data})
    return render_template('upload.html', data=data)


@app.route('/process', methods=['POST'])
def process():
    data=request.form['dat']
    if data:
        #print(data)
        redis_push_data(data)
        #r.set('ipy', data)
        return jsonify({'dat': data})
    return jsonify({'error': "Missing data!"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
