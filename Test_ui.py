import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    """Настройка WebDriver (например, Chrome)"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#           Test_ui_1
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Пле ввода ,текст на кириллице")
@allure.description("Получаем что данные в поле ввода введены на кириллице корректно") 
@allure.feature('Test_ui_1')
def test_input_russian(driver: WebDriver) -> str:
    with allure.step("Шаг 1: Открыть сайт"):
        driver.get("https://market-delivery.yandex.ru/")

    with allure.step("Шаг 2: Найти поле ввода по атрибуту data-testid"):
        search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    with allure.step("Шаг 3: Ввести тестовые данные в поле ввода"):
        test_input = "Пицца"
        search_field.send_keys(test_input)

    with allure.step("Шаг 4: Проверить, что данные были введены правильно"):
        entered_value = search_field.get_attribute("value")
        assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"

#           Test_ui_2   
@allure.epic("Market-Delivery")
@allure.severity (severity_level='crirical') 
@allure.title("Пле ввода ,текст на латинице")
@allure.description("Получаем что данные в поле ввода введены на латиница корректно") 
@allure.feature('Test_ui_2')
def test_input_english(driver: WebDriver) -> str:
    with allure.step("Шаг 1: Открыть сайт"):
        driver.get("https://market-delivery.yandex.ru/")

    with allure.step("Шаг 2: Найти поле ввода по атрибуту data-testid"):
        search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    with allure.step("Шаг 3: Ввести тестовые данные в поле ввода"):
        test_input = "Pizza"
        search_field.send_keys(test_input)

    with allure.step("Шаг 4: Проверить, что данные были введены правильно"):
        entered_value = search_field.get_attribute("value")
        assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"

#           Test_ui_3  
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Пле ввода ,заглавные буквы и прописные на латинице")
@allure.description("Получаем что заглавные буквы и прописные на латинице в поле ввода, введены корректно") 
@allure.feature('Test_ui_3')
def test_input_mixed_case(driver: WebDriver) -> str:
    with allure.step("Шаг 1: Открыть сайт"):
        driver.get("https://market-delivery.yandex.ru/")

    with allure.step("Шаг 2: Найти поле ввода по атрибуту data-testid"):
        search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    with allure.step("Шаг 3: Ввести тестовые данные в поле ввода"):
        test_input = "APPlE"
        search_field.send_keys(test_input)

    with allure.step("Шаг 4: Проверить, что данные были введены правильно"):
        entered_value = search_field.get_attribute("value")
        assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"

#           Test_ui_4 
@allure.epic("Market-Delivery")
@allure.severity (severity_level='crirical') 
@allure.title("Пле ввода ,спецсимволы")
@allure.description("Получаем что спецсимволы введены корректно") 
@allure.feature('Test_ui_4')
def test_input_special_characters(driver: WebDriver) -> str:
    with allure.step("Шаг 1: Открыть сайт"):
        driver.get("https://market-delivery.yandex.ru/")

    with allure.step("Шаг 2: Найти поле ввода по атрибуту data-testid"):
        search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    with allure.step("Шаг 3: Ввести тестовые данные в поле ввода"):
        test_input = "♣☺♂"
        search_field.send_keys(test_input)

    with allure.step("Шаг 4: Проверить, что данные были введены правильно"):
        entered_value = search_field.get_attribute("value")
        assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"

#           Test_ui_5 
@allure.epic("Market-Delivery")
@allure.severity (severity_level='crirical') 
@allure.title("Пле ввода ,цифры в тексте")
@allure.description("Получаем что цифры в тексте введены корректно") 
@allure.feature('Test_ui_5')
def test_input_numeric_text(driver: WebDriver) -> str:
    with allure.step("Шаг 1: Открыть сайт"):
        driver.get("https://market-delivery.yandex.ru/")

    with allure.step("Шаг 2: Найти поле ввода по атрибуту data-testid"):
        search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    with allure.step("Шаг 3: Ввести тестовые данные в поле ввода"):
        test_input = "Добрый Кола без сахара 1.5"
        search_field.send_keys(test_input)

    with allure.step("Шаг 4: Проверить, что данные были введены правильно"):
        entered_value = search_field.get_attribute("value")
        assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"