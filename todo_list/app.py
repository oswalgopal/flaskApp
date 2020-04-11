from flask import Flask, render_template, request

app = Flask(__name__)

todo = []
@app.route('/', methods=["GET", "POST"])
def todo_functon():
    if request.method == "POST":
        todo_name = request.form.get('todo')
        todo.append(todo_name)
    return render_template('index.html', todo=todo)