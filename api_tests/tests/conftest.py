import pytest
import requests
import random
import string
from ..data import BASE_URL, DEFAULT_PASSWORD, DEFAULT_NAME
from ..urls import REGISTER_URL, INGREDIENTS_URL, USER_URL

def generate_unique_email():
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + '@test.com'

def create_user():
    email = generate_unique_email()
    password = DEFAULT_PASSWORD
    name = DEFAULT_NAME
    payload = {'email': email, 'password': password, 'name': name}
    response = requests.post(REGISTER_URL, json=payload)
    if response.status_code != 200:
        raise Exception(f"Failed to create user: {response.status_code}")
    data = response.json()
    access_token = data['accessToken']
    return {'email': email, 'password': password, 'name': name, 'access_token': access_token}

def delete_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(USER_URL, headers=headers)

@pytest.fixture
def user():
    user_data = create_user()
    yield user_data
    delete_user(user_data['access_token'])
def get_ingredients():
    response = requests.get(INGREDIENTS_URL)
    if response.status_code != 200:
        raise Exception(f"Failed to get ingredients: {response.status_code}")
    data = response.json()
    return data['data']