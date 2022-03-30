from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

# Create a class which inherits Resource class from flask_restful
class Greater(Resource):
    def get(self, num1, num2):
        if num1 > num2:
            return num1
        return num2
# Handle all types of data with constructor overloading

api.add_resource(Greater, '/<int:num1>/<int:num2>')

# Test the app
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5001,
        host="0.0.0.0"
    )

