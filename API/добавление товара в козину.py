import requests
import pytest

BASE_URL = "https://www.sibdar-spb.ru"

@pytest.fixture
def api_client():
    """Фикстура для создания HTTP-клиента для API-тестов."""
    session = requests.Session()
    yield session
    session.close()

def test_add_product_to_cart():
   """Проверяет добавление товара в корзину."""
product_id = 180
quantity = 2
payload = {"product_id": product_id, "quantity": quantity}
response = requests.post(f"{BASE_URL}/api/cart/add", data=payload)
assert response.status_code == 200, f"Ошибка: Статус код {response.status_code}"