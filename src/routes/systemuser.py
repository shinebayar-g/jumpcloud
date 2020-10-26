from flask_restful import Resource, reqparse
from requests.exceptions import HTTPError
from sqlalchemy.inspection import inspect
import requests, json

from models.systemuser import SystemUserModel
from util import verify_response


class SystemUser(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('x-api-key', location='headers', required=True)
        self.api_key = self.parser.parse_args()['x-api-key']
        self.request_url = 'https://console.jumpcloud.com/api/systemusers/'
        self.request_headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                                'x-api-key': self.api_key}

    def get(self, user_id):
        self.parser.add_argument('fields', location='args')
        self.parser.add_argument('filter', location='args')
        params = self.parser.parse_args()
        params_filtered = {k: v for k, v in params.items() if v is not None}

        try:
            response = requests.get(self.request_url + user_id,
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

    def delete(self, user_id):

        try:
            response = requests.delete(self.request_url + user_id,
                                       headers=self.request_headers)
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
            user = SystemUserModel.find_by_id(user_id)
            if user:
                user.delete_from_db()
            else:
                return {"error": "User doesn't exist."}, 400
            return verify_response(response), response.status_code

    def put(self, user_id):

        self.parser.add_argument('email', help="Email cannot be blank!")
        self.parser.add_argument('firstname', help="Firstname cannot be blank!")
        self.parser.add_argument('lastname', help="Lastname cannot be blank!")
        self.parser.add_argument('account_locked')
        self.parser.add_argument('activated')
        self.parser.add_argument('suspended')
        data = self.parser.parse_args()
        data_filtered = {k: v for k, v in data.items() if v is not None}

        try:
            response = requests.put(self.request_url + user_id,
                                    headers=self.request_headers,
                                    data=json.dumps(data_filtered))
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
            user = SystemUserModel.find_by_id(user_id)
            table = inspect(SystemUserModel)
            for k, v in data_filtered.items():
                if k in table.c:
                    setattr(user, k, v)
            user.save_to_db()
            return verify_response(response), response.status_code
