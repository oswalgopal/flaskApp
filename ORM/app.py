import os
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://postgres:1234@localhost:3000/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

@app.route('/')
def index():
    db.create_all() # to create a table on the basis of the class
    db.session.commit() # commit the changes to the database
    return 'True'
    
@app.route('/adduser/<int:id>')
def adduser(id):
    tempuser = User(id=id, name='Gopal', mobile='2024415907')
    db.session.add(tempuser)
    db.session.commit()
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/getuser')
def getuser():
    users = User.query.all()
    return render_template('index.html', users=users)