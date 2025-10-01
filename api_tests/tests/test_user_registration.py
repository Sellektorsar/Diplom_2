import pytest
import requests
import allure
from .conftest import generate_unique_email
from ..data import DEFAULT_PASSWORD, DEFAULT_NAME, ERROR_USER_EXISTS, ERROR_MISSING_FIELDS
from ..urls import REGISTER_URL

class TestUserRegistration:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self):
        email = generate_unique_email()
        payload = {'email': email, 'password': DEFAULT_PASSWORD, 'name': DEFAULT_NAME}
        response = requests.post(REGISTER_URL, json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data['success'] == True
        assert 'user' in data
        assert 'accessToken' in data
        assert 'refreshToken' in data

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self):
        email = generate_unique_email()
        payload = {'email': email, 'password': DEFAULT_PASSWORD, 'name': DEFAULT_NAME}
        # Создать первого
        requests.post(REGISTER_URL, json=payload)
        # Попытаться создать второго
        response = requests.post(REGISTER_URL, json=payload)
        assert response.status_code == 403
        data = response.json()
        assert data['success'] == False
        assert data['message'] == ERROR_USER_EXISTS

    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_create_user_missing_field(self, missing_field):
        email = generate_unique_email()
        payload = {'email': email, 'password': DEFAULT_PASSWORD, 'name': DEFAULT_NAME}
        del payload[missing_field]
        response = requests.post(REGISTER_URL, json=payload)
        assert response.status_code == 403
        data = response.json()
        assert data['success'] == False
        assert data['message'] == ERROR_MISSING_FIELDS