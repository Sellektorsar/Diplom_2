import pytest
import requests
import allure
from .conftest import get_ingredients
from ..data import ERROR_UNAUTHORIZED
from ..urls import ORDERS_URL

class TestUserOrders:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_authorized(self, user):
        # Сначала создать заказ
        ingredients = get_ingredients()
        payload = {'ingredients': [ingredients[0]['_id']]}
        headers = {'Authorization': user['access_token']}
        requests.post(ORDERS_URL, json=payload, headers=headers)
        # Теперь получить заказы
        response = requests.get(ORDERS_URL, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data['success'] == True
        assert 'orders' in data
        assert isinstance(data['orders'], list)

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_unauthorized(self):
        response = requests.get(ORDERS_URL)
        assert response.status_code == 401
        data = response.json()
        assert data['success'] == False
        assert data['message'] == ERROR_UNAUTHORIZED