from flask import request
from flask_restful import Resource

from services.user import UserServices


class UserHandler(Resource):
    '''
    This layer handles all interaction with the clients - requests & responses
    '''

    # get credential when users log in to check with the db
    def get(self):
        credentials = request.get_json()
        if UserServices.check_permission(credentials['emp_id'], credentials['password']):
            return {"message": "Login successfully"}, 200
        return {"message": "Login failed"}, 404

    # get information to register a new user
    def post(self):
        user_info = request.get_json()
        UserServices.add_user(user_info)
        return {"message": f"Employee with emp_id {user_info['emp_id']} is created successfully"}, 200
