from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import requests, json
from requests.exceptions import HTTPError

app = Flask(__name__)
api = Api(app)


# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jumpcloud:PHbnDDB8yFnvCQVK@localhost:3306/jumpcloud'
#
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     location = db.Column(db.String(50))
#     date_created = db.Column(db.DateTime, default=datetime.now)
#
#
#     db.session.add(user)
#     db.session.commit()
#
#     user = User.query.filter_by(name=name).first()
#

def verify_response(response):
    try:
        return response.json()
    except ValueError:
        return {"message": response.text}

class Info(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('x-api-key', location='headers', required=True)
        self.api_key = self.parser.parse_args()['x-api-key']
        self.request_url = 'https://console.jumpcloud.com/api/systemusers'
        self.request_headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                                'x-api-key': self.api_key}



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
            return verify_response(response), response.status_code


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
            return verify_response(response), response.status_code

    def put(self, user_id):

        self.parser.add_argument('email', help="Email cannot be blank!")
        self.parser.add_argument('firstname', help="Firstname cannot be blank!")
        self.parser.add_argument('lastname', help="Lastname cannot be blank!")
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
            return verify_response(response), response.status_code


api.add_resource(SystemUsers, '/api/v1.0/systemusers')
api.add_resource(SystemUser, '/api/v1.0/systemusers/<user_id>')
api.add_resource(Info, '/api/v1.0/info')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
