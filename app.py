
# importing my own libraries to make my own api
from flask import Flask, jsonify, request,render_template,session, redirect, url_for,json
from bson.json_util import dumps
from bson.objectid import ObjectId
#from user.models import User
from flask_pymongo import PyMongo
import bson
from pymongo import MongoClient
from flask_restful import Resource, Api
from flask.json import JSONEncoder

from bson import json_util


# define a custom encoder point to the json_util provided by pymongo (or its dependency bson)
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj): return json_util.default(obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.secret_key = 'some secret key'
#app.secret.key = "secretkey"
app.config['MONGO_URI'] = 'mongodb://localhost:27017/user'
mongo = PyMongo(app)


@app.route('/add', methods=['POST'])
def post_framework():
    framework = mongo.db.frameworks
    username = request.json['username']
    password = request.json['password']
    email =request.json['email']

    framework_id = framework.insert({'username': username, 'password': password, 'email':email})
    new_framework = framework.find_one({'_id': framework_id})

    output = {'username': new_framework['username'], 'password': new_framework['password'],'email':new_framework['email']}

    return jsonify({'result ': output})

@app.route('/findall', methods=['POST'])
def logins():
    user_records = mongo.db.frameworks.find({'username': request.json['username']})
    return dumps(user_records)



@app.route('/users', methods = ["GET"])
def users():
    users = mongo.db.user.frameworks.find()
    resp = dumps(users, sort_keys = True, indent = 5 )
    return jsonify(resp)

@app.route('/finds/username/<string:username>' , methods=["POST"])
def page(username):
    _json = request.json
    page = mongo.db.frameworks.find_one({'username':username})
    resp = json.dumps(page)
    return jsonify(resp)




if __name__ == "__main__":
    app.run(debug=True)
