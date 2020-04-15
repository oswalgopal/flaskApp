from flask_sqlalchemy import SQLAlchemy # importing SQLAlchemy from flask_sqlalchemy
db = SQLAlchemy() # creating an instance of SQLAlchemy


# ppt url (https://cdn.cs50.net/web/2018/spring/lectures/4/lecture4.pdf)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, nullable=True)
    mobile= db.Column(db.String, nullable=True)