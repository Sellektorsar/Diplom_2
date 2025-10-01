import pytest
import requests
import allure
from .conftest import generate_unique_email
from ..data import DEFAULT_PASSWORD, DEFAULT_NAME, ERROR_UNAUTHORIZED
from ..urls import USER_URL

class TestUserUpdate:

    @allure.title('Изменение email с авторизацией')
    def test_update_email_authorized(self, user):
        new_email = generate_unique_email()
        payload = {'email': new_email}
        headers = {'Authorization': user['access_token']}
        response = requests.patch(USER_URL, json=payload, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data['success'] == True
        assert data['user']['email'] == new_email

    @allure.title('Изменение password с авторизацией')
    def test_update_password_authorized(self, user):
        new_password = DEFAULT_PASSWORD + 'new'
        payload = {'password': new_password}
        headers = {'Authorization': user['access_token']}
        response = requests.patch(USER_URL, json=payload, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data['success'] == True
        # Пароль не возвращается, но success true

    @allure.title('Изменение name с авторизацией')
    def test_update_name_authorized(self, user):
        new_name = DEFAULT_NAME + 'Updated'
        payload = {'name': new_name}
        headers = {'Authorization': user['access_token']}
        response = requests.patch(USER_URL, json=payload, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data['success'] == True
        assert data['user']['name'] == new_name

    @allure.title('Изменение email без авторизации')
    def test_update_email_unauthorized(self):
        new_email = generate_unique_email()
        payload = {'email': new_email}
        response = requests.patch(USER_URL, json=payload)
        assert response.status_code == 401
        data = response.json()
        assert data['success'] == False
        assert data['message'] == ERROR_UNAUTHORIZED

    @allure.title('Изменение password без авторизации')
    def test_update_password_unauthorized(self):
        new_password = DEFAULT_PASSWORD + 'new'
        payload = {'password': new_password}
        response = requests.patch(USER_URL, json=payload)
        assert response.status_code == 401
        data = response.json()
        assert data['success'] == False
        assert data['message'] == ERROR_UNAUTHORIZED

    @allure.title('Изменение name без авторизации')
    def test_update_name_unauthorized(self):
        new_name = DEFAULT_NAME + 'New'
        payload = {'name': new_name}
        response = requests.patch(USER_URL, json=payload)
        assert response.status_code == 401
        data = response.json()
        assert data['success'] == False
        assert data['message'] == ERROR_UNAUTHORIZED