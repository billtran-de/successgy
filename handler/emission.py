from flask import request
from flask_restful import Resource

from services.emission import EmissionServices


class EmissionHandler(Resource):
    '''
    This layer handles all interaction with the clients - requests & responses
    '''

    # get information to register a new user
    def post(self):
        emission_data = request.get_json()
        EmissionServices.add_emission_record(emission_data)
        return {"message": "emission data is created successfully"}, 200

    def get(self):
        emission_source = request.args.get('emission_source')
        emission_data = EmissionServices.get_emission_table(emission_source)
        return {"data": emission_data}, 200
