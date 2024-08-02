from flask import Flask, render_template,url_for,request,redirect,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors,re,hashlib
from database import get_data

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Benita@3216'
app.config['MYSQL_DB'] = 'event_manager'

mysql = MySQL(app)


@app.route('/event_manager/', methods=['GET', 'POST'])
def login():
    
    
    msg = ''
   
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        
        username = request.form['username']
        password = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password,))
       
        user = cursor.fetchone()
        
        if user:
           
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']

            return render_template('landing.html', msg=msg)
           
        else:
            
            msg = 'Incorrect username/password!'
    
    return render_template('home.html')

@app.route('/project/register', methods=['GET', 'POST'])
def register():
   
    msg = ''
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pythonlogin WHERE username = %s', (username,))
        pythonlogin = cursor.fetchone()
        
        if pythonlogin:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
           
            hash = password + app.secret_key
            hash = hashlib.sha1(hash.encode())
            password = hash.hexdigest()
            
            cursor.execute('INSERT INTO pythonlogin VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'

            
    elif request.method == 'POST':
       
        msg = 'Please fill out the form!'
    
    return render_template('main.html', msg=msg)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/event_manager/landing')
def landing():
    return render_template('landing.html')


@app.route('/signin',methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@app.route('/getstarted')
def getstarted():
    return render_template('getstarted.html')
@app.route('/events')
def events():
     data = get_data()
     return render_template('events.html',data=data)
@app.route('/eventcreation')
def eventcreation():
    return render_template('eventcreation.html')
@app.route('/event_manager/user')
def user():
     data = get_data()
     return render_template('user.html',data=data)

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