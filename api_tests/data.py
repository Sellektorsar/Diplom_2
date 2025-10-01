BASE_URL = 'https://stellarburgers.nomoreparties.site/api'

DEFAULT_PASSWORD = 'password123'
DEFAULT_NAME = 'TestUser'

# Тестовые данные для пользователей
USER_DATA = {
    'email': 'test-data@yandex.ru',
    'password': DEFAULT_PASSWORD,
    'name': DEFAULT_NAME
}

INVALID_EMAIL = 'invalid@test.com'
INVALID_PASSWORD = 'wrongpassword'

# Сообщения об ошибках
ERROR_USER_EXISTS = 'User already exists'
ERROR_MISSING_FIELDS = 'Email, password and name are required fields'
ERROR_INVALID_CREDENTIALS = 'email or password are incorrect'
ERROR_UNAUTHORIZED = 'You should be authorised'
ERROR_INGREDIENT_IDS_REQUIRED = 'Ingredient ids must be provided'