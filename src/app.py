from flask import Flask, request, escape
import requests
import json


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1.0/systemusers', methods=['GET', 'POST'])
def systemusers():
    if request.method == 'GET':
        response = requests.get('https://console.jumpcloud.com/api/systemusers',
                                headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': 'f78a87270171adf8e8ae827565fee1acbca60d1a'})
        return response.json()
    elif request.method == 'POST':
        username = escape(request.form['username'])
        email = escape(request.form['email'])
        firstname = escape(request.form['firstname'])
        lastname = escape(request.form['lastname'])
        response = requests.post('https://console.jumpcloud.com/api/systemusers',
                                 headers={'Accept': 'application/json', 'Content-Type': 'application/json',
                                          'x-api-key': 'f78a87270171adf8e8ae827565fee1acbca60d1a'},
                                 data=json.dumps({'username': username, 'email': email, 'firstname': firstname, 'lastname': lastname}))
        return response.json()


@app.route('/api/v1.0/systemusers/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def systemuser(user_id):
    if request.method == 'GET':
        response = requests.get(f'https://console.jumpcloud.com/api/systemusers/{user_id}',
                                headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': 'f78a87270171adf8e8ae827565fee1acbca60d1a'})
        return response.json()
    elif request.method == 'PUT':
        email = escape(request.form['email'])
        firstname = escape(request.form['firstname'])
        lastname = escape(request.form['lastname'])
        response = requests.put(f'https://console.jumpcloud.com/api/systemusers/{user_id}',
                                headers={'Accept': 'application/json', 'Content-Type': 'application/json',
                                         'x-api-key': 'f78a87270171adf8e8ae827565fee1acbca60d1a'},
                                data=json.dumps({'email': email, 'firstname': firstname, 'lastname': lastname}))
        return response.json()
    elif request.method == 'DELETE':
        response = requests.delete(f'https://console.jumpcloud.com/api/systemusers/{user_id}',
                                   headers={'Accept': 'application/json', 'Content-Type': 'application/json',
                                            'x-api-key': 'f78a87270171adf8e8ae827565fee1acbca60d1a'})
        return response.json()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
