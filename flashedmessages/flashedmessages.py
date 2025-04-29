from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    return render_template('index9.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    errormsg = None

    if request.method = 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            errormsg = 'Invalid username or password. Please try again'
        else:
            flash('You are sucessfully logged in') # 消息闪现，把这句话再次放进 request 里面，到 index 里面后，进入 index9.html 会把这句话打印下来
            return redirect(url_for('index'))

    return render_template('login9.html', error = errormsg)

if __name__ == "__main__":
    app.run(debug = True, threaded = True)























