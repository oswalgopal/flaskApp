from flask import Flask, render_template

app = Flask(__name__)

todo = ['task 1', 'task 2', 'task 3', 'task 4']
@app.route('/')
def todo_functon():
    return render_template('index.html', todo=todo)