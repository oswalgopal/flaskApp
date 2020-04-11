from flask import Flask, render_template, request, session #imported the session from the flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oswalgopal'
@app.route('/', methods=['POST', 'GET'])
def getName():
    # if session["notes"] is None: # created a session array if that array doesnot exist
    #     session["notes"] = []
    #     print('if worked')
    if request.method == 'POST':
        name = request.form.get('name')
        session["notes"].append(name)
    if request.method == 'GET':
        print('')
        session["notes"] = session["notes"]
    return render_template('index.html', array=[])