# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Calculator API'})

@app.route('/add')
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'result': a + b})

if __name__ == '__main__':
    app.run(debug=True)