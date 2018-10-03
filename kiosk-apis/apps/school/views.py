from flask import Blueprint
import flask_restful
from flask_restful import reqparse
from requests.auth import HTTPBasicAuth
import config
import requests

API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1

version3_school = Blueprint('version3_school', __name__)
api_v1 = flask_restful.Api(version3_school)


class PersonsList(flask_restful.Resource):

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('first_name', type=str)
        parse.add_argument('last_name', type=str)
        parse.add_argument('dob', type=str)
        parse.add_argument('guid', type=str)
        parse.add_argument('person_number', type=str)
        parse.add_argument('start', type=str)
        parse.add_argument('end', type=str)
        parse.add_argument('telephone_number', type=str)
        args = parse.parse_args()
        print(args)
        payload = {'firstName': args['first_name'], 'lastName': args['last_name'], 'dateOfBirth': args['dob'],
                   'personNumber': args['person_number'], 'telephoneNumber': args['telephone_number'],
                   'start': args['start'], 'end': args['end'], 'guid': args['guid']}
        headers = {'ApplicationKey': 'version3'}
        response = requests.get(config.VERSION3_SCHOOL_SANDBOX + config.VERSION3_PERSONLIST_API, params=payload,
                                auth=HTTPBasicAuth(config.VERSION3_SCHOOL_USERNAME, config.VERSION3_SCHOOL_PASSWORD),
                                headers=headers)
        if response.status_code == 200:
            return {"person_data": response.json()}
        else:
            return {"message": "Something went wrong", "status": response.status_code}


api_v1.add_resource(PersonsList, '/persons')


class TeachersList(flask_restful.Resource):

    def get(self):
        pass


api_v1.add_resource(TeachersList, '/teachers')


class StudentsList(flask_restful.Resource):

    def get(self):
        pass


api_v1.add_resource(StudentsList, '/students')
