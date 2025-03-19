import requests
import pytest

BASE_URL = "https://www.sibdar-spb.ru"

@pytest.fixture
def api_client():
    """Фикстура для создания HTTP-клиента для API-тестов."""
    session = requests.Session()
    yield session
    session.close()

def test_remove_product_from_cart():
   """Проверяет удаление товара из корзины."""
product_id =180
response = requests.delete(f"{BASE_URL}/api/cart/remove/{product_id}")
assert response.status_code == 200, f"Ошибка: Статус код {response.status_code}"
