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
@allure.story("Добавление товара в корзину")
def test_add_to_cart(driver):
    with allure.step("Открываем главную страницу"):
        driver.get(BASE_URL)

    with allure.step("Ждем, пока кнопка 'В корзину' станет кликабельной, и кликаем"):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[1]/div[3]/button"))
        ).click()

    with allure.step("Добавляем 2 гриба в корзину"):
        add_grib = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div[3]/button")
        add_grib.click()
        add_grib.click()

    with allure.step("Открываем корзину"):
        driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/a/div[2]").click()

    with allure.step("Смотрим что лежит в корзине"):
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//несуществующий_элемент"))
            )
        except:
            pass
