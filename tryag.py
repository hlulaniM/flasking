# importing my own libraries to make my own api
from flask import Flask, jsonify,request
from flask_restful import Resource,Api

#creating api object
app = Flask(_name_)
api = Api(app)

#defining a class with a method get , returning a json object

class HelloWorld(Resource):
	def _init_(self):
		pass
	def get(self):
	    return{
		"Hello":"World"}

api.add_resource(HelloWorld,'/')
if _name_ == "_main_":
   app.run(debug=True)