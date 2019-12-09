from flask import render_template, flash, redirect, Config, jsonify
from main_app import *
from forms import LoginForm

'''

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/void')
    return render_template('void.html', title='Sign In', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error=None
    if request.method == 'POST':
        if valud_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else: error="Invalid username/password"
    return render_template('login.html', error=error)

'''
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
        #new_data=data[::-1]
        #print(data)
        redis_push_data(data)
        #r.set('ipy', data)
        return jsonify({'dat': data})
    return jsonify({'error': "Missing data!"})
