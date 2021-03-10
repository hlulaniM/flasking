
from flask import Flask, jsonify , requests
from flask_restful import Resource,Api

#creating api object

app = Flask(__name__)
api = Api(app)

Data ={}
#defining a class with a method get , returning a json object
class HelloWorld(Resource):
	def __init__(self):
		pass
	def POST(self,username ,password ):
		Tem = {'username':username , 'password':password}
		Data.append(Tem)
		return "Welcome " + Tem
api.add_resource(HelloWorld,'/route/<string:username> /<string:password>')

if __name__ == "__main__":
	app.run(debug =True)