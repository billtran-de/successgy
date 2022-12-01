from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from handler.user import UserHandler
from handler.emission import EmissionHandler

# initialize Flask API
app = Flask(__name__)
CORS(app)
api = Api(app)

# add route
api.add_resource(UserHandler, '/api/user')
api.add_resource(EmissionHandler, '/api/emission')

if __name__ == '__main__':
    app.run(debug=True)
