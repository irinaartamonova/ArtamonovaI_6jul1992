import requests
import pytest

BASE_URL = "https://www.sibdar-spb.ru"

@pytest.fixture
def api_client():
    """Фикстура для создания HTTP-клиента для API-тестов."""
    session = requests.Session()
    yield session
    session.close()

def test_get_cart_contents():
    """Проверяет получение содержимого корзины."""
response = requests.get(f"{BASE_URL}/api/cart")
assert response.status_code == 200, f"Ошибка: Статус код {response.status_code}"