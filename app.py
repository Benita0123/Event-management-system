
from flask import Flask, render_template,url_for,request
from database import get_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/getstarted')
def getstarted():
    return render_template('getstarted.html')
@app.route('/events')
def events():
    return render_template('events.html')
@app.route('/eventcreation')
def eventcreation():
    return render_template('eventcreation.html')
@app.route('/event_manager/user')
def user():
    return render_template('user.html')

@app.route('/event_manager/base')
def base():
    return render_template('base.html')

@app.route('/event_manager/profile')
def profile():
    return render_template('profile.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
    

from flask import Flask, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
