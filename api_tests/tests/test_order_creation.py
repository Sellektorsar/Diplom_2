import pytest
import requests
import allure
from .conftest import get_ingredients
from ..data import ERROR_UNAUTHORIZED, ERROR_INGREDIENT_IDS_REQUIRED
from ..urls import ORDERS_URL

class TestOrderCreation:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_authorized_with_ingredients(self, user):
        ingredients = get_ingredients()
        payload = {'ingredients': [ingredients[0]['_id'], ingredients[1]['_id']]}
        headers = {'Authorization': user['access_token']}
        response = requests.post(ORDERS_URL, json=payload, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data['success'] == True
        assert 'order' in data
        assert 'number' in data['order']

    @allure.title('Создание заказа без авторизации')
    def test_create_order_unauthorized(self):
        ingredients = get_ingredients()
        payload = {'ingredients': [ingredients[0]['_id']]}
        response = requests.post(ORDERS_URL, json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data['success'] == True
        assert 'order' in data
        assert 'number' in data['order']

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_no_ingredients(self, user):
        payload = {'ingredients': []}
        headers = {'Authorization': user['access_token']}
        response = requests.post(ORDERS_URL, json=payload, headers=headers)
        assert response.status_code == 400
        data = response.json()
        assert data['success'] == False
        assert data['message'] == ERROR_INGREDIENT_IDS_REQUIRED

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_ingredient_hash(self, user):
        payload = {'ingredients': ['invalidhash']}
        headers = {'Authorization': user['access_token']}
        response = requests.post(ORDERS_URL, json=payload, headers=headers)
        assert response.status_code == 500