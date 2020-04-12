from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
# hostname: oswalgopal-database.cmhbhrlpytbe.ap-south-1.rds.amazonaws.com
# password: oswalgopal25052000
engine = create_engine('postgresql://oswalgopal:oswalgopal25052000@oswalgopal-database.cmhbhrlpytbe.ap-south-1.rds.amazonaws.com:5432/loginPanel')
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')