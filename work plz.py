# importing my own libraries to make my own api
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)


@app.route('/display', methods=['POST'])
def display():
    data = request.get_json()
    username = data['username']
    password = data['password']
    return jsonify({'username': username, 'password': password})


if __name__ == "__main__":
    app.run(debug=True)
