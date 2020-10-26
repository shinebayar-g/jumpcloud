import os
from flask_restful import Resource, reqparse

from models.systemuser import SystemUserModel


class Info(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('x-api-key', location='headers', required=True)
        self.api_key = self.parser.parse_args()['x-api-key']

    def get(self):
        if self.api_key != os.environ.get('X_API_KEY'):
            print(os.environ.get('X_API_KEY'))
            return {"error": "Authentication failed."}, 401

        all_users = SystemUserModel.query.all()
        gmail_users = SystemUserModel.query.filter(SystemUserModel.email.endswith('@gmail.com')).all()
        locked_users = SystemUserModel.query.filter_by(account_locked="true").all()
        suspended_users = SystemUserModel.query.filter_by(suspended="true").all()
        activated_users = SystemUserModel.query.filter_by(activated="true").all()

        return {"total": len(all_users),
                "all_users": [i.serialize for i in all_users],
                "gmail_users": [i.serialize for i in gmail_users],
                "locked_users": [i.serialize for i in locked_users],
                "suspended_users": [i.serialize for i in suspended_users],
                "activated_users": [i.serialize for i in activated_users], }
