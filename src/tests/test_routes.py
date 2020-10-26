import os

import requests

api_key = os.environ.get('X_API_KEY')
request_base_url = 'http://127.0.0.1:5000/api/v1.0/'
request_headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                   'x-api-key': api_key}


def test_get_systemusers():
    response = requests.get(request_base_url + 'info',
                            headers=request_headers)
    assert response.status_code == 200


def test_get_info():
    response = requests.get(request_base_url + 'info',
                            headers=request_headers)
    print(response.text)
    print(response.url)
    assert response.status_code == 200
