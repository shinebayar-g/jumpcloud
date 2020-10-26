import json

from flask_restful import Resource, reqparse
from requests.exceptions import HTTPError
import requests

from models.systemuser import SystemUserModel
from util import verify_response


class SystemUsers(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('x-api-key', location='headers', required=True)
        self.api_key = self.parser.parse_args()['x-api-key']
        self.request_url = 'https://console.jumpcloud.com/api/systemusers'
        self.request_headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                                'x-api-key': self.api_key}

    def get(self):
        self.parser.add_argument('filter', location='args')
        self.parser.add_argument('search', location='args')
        self.parser.add_argument('limit', type=int, location='args')
        self.parser.add_argument('skip', type=int, location='args')
        self.parser.add_argument('sort', location='args')
        self.parser.add_argument('fields', location='args')
        params = self.parser.parse_args()
        params_filtered = {k: v for k, v in params.items() if v is not None}

        try:
            response = requests.get(self.request_url,
                                    headers=self.request_headers,
                                    params=params_filtered)
            try:
                response.raise_for_status()
            except HTTPError:
                return verify_response(response), response.status_code
            except Exception as err:
                return {"error": err}
        except HTTPError as http_err:
            return {"error": str(http_err)}
        except Exception as err:
            return {"error": str(err)}
        else:
            return verify_response(response), response.status_code

    def post(self):
        self.parser.add_argument('username', required=True, help="Username cannot be blank!")
        self.parser.add_argument('email', required=True, help="Email cannot be blank!")
        self.parser.add_argument('firstname', required=True, help="Firstname cannot be blank!")
        self.parser.add_argument('lastname', required=True, help="Lastname cannot be blank!")
        self.parser.add_argument('account_locked')
        self.parser.add_argument('activated')
        self.parser.add_argument('suspended')
        data = self.parser.parse_args()

        try:
            response = requests.post(self.request_url,
                                     headers=self.request_headers,
                                     data=json.dumps(data))
            try:
                response.raise_for_status()
            except HTTPError:
                return verify_response(response), response.status_code
            except Exception as err:
                return {"error": err}
        except HTTPError as http_err:
            return {"error": str(http_err)}
        except Exception as err:
            return {"error": str(err)}
        else:
            user = SystemUserModel(response.json())
            user.save_to_db()
            return verify_response(response), response.status_code
