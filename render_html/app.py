import datetime  # to get time we import it from python
from flask import Flask, render_template #render template is a function to render the templates onto the web page

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html') # add index.html in templates folder so that flask can render the html file

@app.route('/<string:name>')
def name_function(name):
    time = datetime.datetime.now() # pre defined functions in python for the time
    return render_template('name.html', name=name.capitalize(), time=time)

@app.route('/If_Else=<string:if_else>')
def if_else(if_else):
    return render_template('if_else.html', if_else=if_else.upper())