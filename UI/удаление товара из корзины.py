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
@allure.feature("Корзина")
@allure.story("Удаление товара из корзины")
def test_delete_from_cart(driver):
    with allure.step("Открываем главную страницу"):
        driver.get(BASE_URL)

    with allure.step("Добавляем грибы в корзину"):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div[3]/button"))
        ).click()

    with allure.step("Ждем и открываем корзину"):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div[2]/div/a/div[2]"))
        ).click()

    with allure.step("Удаляем товар из корзины"):
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form/div[1]/div/div[2]/button").click()

    with allure.step("Смотрим на корзину"):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//несуществующий_элемент"))
            )
        except:
            pass

