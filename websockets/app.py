from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO,emit
app = Flask(__name__)
socketIo = SocketIO(app)
messages = []
@app.route('/')
def index():
    return render_template('index.html')

@socketIo.on('message')
def message(data):
    message = data['message']
    messages.append(message)
    emit('messageAll', message, broadcast=True)
