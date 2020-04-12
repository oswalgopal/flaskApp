from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
# hostname: oswalgopal-database.cmhbhrlpytbe.ap-south-1.rds.amazonaws.com
# password: oswalgopal25052000
engine = create_engine('postgresql://oswalgopal:oswalgopal25052000@oswalgopal-database.cmhbhrlpytbe.ap-south-1.rds.amazonaws.com:5432/loginPanel')
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
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
    return render_template('home')

@app.errorhandler(404)
def error(error):
    return render_template('404.html')