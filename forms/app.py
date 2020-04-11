from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def getName():
    name = request.form.get('name')
    return render_template('index.html', name=name)