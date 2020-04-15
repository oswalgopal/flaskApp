from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'Response': 'Server is running perfect',
        "status": 200,
        'message': "OK"
        })