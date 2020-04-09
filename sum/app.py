# @author: Gopal Oswal
# @date: 9 April 2020
# @description: basic sum using the flask app

from flask import Flask
app = Flask(__name__)

@app.route('/')
def baseRoute():
    return 'server is running'

# adding the variables name in the url to get the value
# syntax is <converter: variable_name>
@app.route('/numberOne=<int:a>&numberTwo=<int:b>')
def sum(a,b):
    return f'Sum of {a} and {b} is {a + b}'
