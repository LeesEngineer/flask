from flask import Falsk
from flask import render_template
from flask import request
from flask import Flask, session, redirect, url_for, reqeust

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    if 'username' in session;
        user = session['username']
        return 'user is' + user + '<br>' + "<b><a href = '/logout'>Click here to logout</a></b>"
    return "You didn't login, <br><a href = 'login'><b>Click here to login</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('index7.html')

@qpp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True, threaded = True)
