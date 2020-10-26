import os
from flask import Flask
from flask_restful import Api

from routes.systemuser import SystemUser
from routes.systemusers import SystemUsers
from routes.info import Info

app = Flask(__name__)
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_CHARSET'] = 'utf8mb4'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(SystemUsers, '/api/v1.0/systemusers')
api.add_resource(SystemUser, '/api/v1.0/systemusers/<user_id>')
api.add_resource(Info, '/api/v1.0/info')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(host='0.0.0.0')
