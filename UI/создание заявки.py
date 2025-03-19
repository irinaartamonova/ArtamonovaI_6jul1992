import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.sibdar-spb.ru/"


@pytest.fixture(scope="session")
def driver():
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.ui
@allure.feature("Оформление заказа")
@allure.story("Создание заявки")
def test_create_request(driver):
    with allure.step("Открываем главную страницу"):
        driver.get(BASE_URL)

    with allure.step("Добавляем товар в корзину"):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div[3]/button"))
        ).click()

    with allure.step("Открываем корзину"):
        driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/a/div[1]").click()

    with allure.step("Заполняем поле с именем"):
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form/div[2]/div[1]/div[1]/input").send_keys("Илья")

    with allure.step("Заполняем поле с телефоном"):
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form/div[2]/div[1]/div[2]/input").send_keys(
            "+9601359776")

    with allure.step("Кликаем на кнопку 'Отправить'"):
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form/div[2]/div[2]/p/button").click()

    with allure.step("Смотрим 5 секунд"):
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//несуществующий_элемент"))
            )
        except:
            pass
        