from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine('postgresql://oswalgopal:oswalgopal25052000@oswalgopal-database.cmhbhrlpytbe.ap-south-1.rds.amazonaws.com:5432/loginPanel')
db = scoped_session(sessionmaker(bind=engine))

app.secret_key = 'OswalGopal'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    if session.get('loginStatus') == True:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if session.get('loginStatus') == True:
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        userdata = db.execute('SELECT * FROM  public.user where username = :username and password = :password' ,
        {"username": username, "password": password}).fetchall()
        if len(userdata) > 0:
            session['loginStatus'] = True
            return redirect(url_for('home'))
        else: 
            return render_template('error.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if session.get('loginStatus') == True:
            return redirect(url_for('home'))
        else:
            return render_template('register.html')
    else:
        password = request.form.get('password')
        confirmpassord = request.form.get('confirmpassword')
        if password == confirmpassord:
            name = request.form.get('name')
            mobile = request.form.get('mobile')
            username = request.form.get('username')
            db.execute('INSERT INTO public.user (username, password, name, mobile) VALUES (:username, :password, :name, :mobile)',
             {"username": username, "password": password, "name": name, "mobile": mobile})
            db.commit()
            return redirect(url_for('home'))
        else:
            return render_template('register.html')

@app.route('/home')
def home():
    if session.get('loginStatus') == True:
        userdata = db.execute('SELECT * FROM  public.user').fetchall()
        return render_template('home.html', userdata=userdata)
    else: 
        return redirect(url_for('login'))

@app.errorhandler(404)
def error(error):
    return render_template('404.html')

@app.route('/logout', methods=['POST'])
def logout():
    session['loginStatus'] = False
    return redirect(url_for('login'))