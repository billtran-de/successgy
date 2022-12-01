from flask import request
from flask_restful import Resource

# from services.user import UserServices


class EnergySourceHandler(Resource):
    '''
    This layer handles all interaction with the clients - requests & responses
    '''

    # get information to register a new user
    def post(self):
        energy_info = request.get_json()
        print(energy_info)
