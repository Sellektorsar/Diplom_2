import pytest
import requests
import allure
from ..data import INVALID_EMAIL, INVALID_PASSWORD, ERROR_INVALID_CREDENTIALS
from ..urls import LOGIN_URL

class TestUserLogin:

    @allure.title('Логин под существующим пользователем')
    def test_login_existing_user(self, user):
        payload = {'email': user['email'], 'password': user['password']}
        response = requests.post(LOGIN_URL, json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data['success'] == True
        assert 'user' in data
        assert 'accessToken' in data
        assert 'refreshToken' in data

    @allure.title('Логин с неверным логином и паролем')
    def test_login_invalid_credentials(self):
        payload = {'email': INVALID_EMAIL, 'password': INVALID_PASSWORD}
        response = requests.post(LOGIN_URL, json=payload)
        assert response.status_code == 401
        data = response.json()
        assert data['success'] == False
        assert data['message'] == ERROR_INVALID_CREDENTIALS