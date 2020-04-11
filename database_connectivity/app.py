import os # imported os from python
from flask import Flask, render_template, request
from sqlalchemy import create_engine # imported create_engine from sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker # imported scoped_session , sessionmaker from sqlalchemy.orm 

app = Flask(__name__)

engine = create_engine('postgresql://postgres:1234@localhost:3000/postgres')  # created an engine with the url to the database
db = scoped_session(sessionmaker(bind=engine)) # created an scooped session with sessionmaker and our engine

@app.route('/')
def index():
    test = db.execute("SELECT * FROM test").fetchall()
    return render_template('index.html', data=test)

