import pytest
import requests
import allure

# Базовый URL
BASE_URL = "https://market-delivery.yandex.ru/eats/v1/full-text-search/v1"
"""Базовый URL https://market-delivery.yandex.ru/eats/v1/full-text-search/v1"""

# Общие заголовки
HEADERS = {
    "location": "longitude=37.65258868982598&latitude=55.73880923260818",
    "Apikey": "c0d403ab-e5be-4049-908c-8122a58acf23",
    "latitude": "55.73880923260818",
    "longitude": "37.65258868982598",
    "Content-Type": "application/json"
}
"""Общие заголовки"""

# Тесты для каждого запроса

#           Test_Api_1 Несколько слов в названии товара
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Пле ввода ,несколько слов в названии товара")
@allure.description("Получаем что поле ввода принимает корректно текст из двух слов") 
@allure.feature('Test_Api_1')
def test_few_words_in_the_product_name():
    with allure.step("1. Запрос: ""несколько слов в названии товара"):
        payload = {
        "text": "Соус Барбекю",
        "region_id": 20
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

#           Test_Api_2 Точное название товара
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Пле ввода ,Точное название товара")
@allure.description("Получаем что поле ввода принимает корректные тестовые данные") 
@allure.feature('Test_Api_2')
def test_exact_product_name():
    with allure.step("2. Запрос:" "Точное название товара"):
        payload = {
        "text": "Мороженое ванильное «Вологодский пломбир»",
        "region_id": 20
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

#           Test_Api_3 Наличие товара по запросу
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Наличие товара по запросу")
@allure.description("Получаем товар на запросу текстом") 
@allure.feature('Test_Api_3')
def test_product_availability_upon_request():
    with allure.step("3. Запрос:" "Наличие товара по запросу"):
        payload = {
        "text": "мороженое",
        "region_id": 20
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

#           Test_Api_4 Кириллица и латиница
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Кириллица и латиница")
@allure.description("Получаем товар с названием на латинице") 
@allure.feature('Test_Api_4')
def test_search_cyrillic_and_latin():
    with allure.step("4. Запрос:" "Кириллица и латиница"):
        payload = {
        "text": "Pepsi",
        "region_id": 20
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

#           Test_Api_5 Найти товар по ID
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Найти товар по ID")
@allure.description("Получаем товар через ID товара") 
@allure.feature('Test_Api_5')
def test_find_product_by_number():
    with allure.step("5. Запрос:" "Найти товар по ID"):
        payload = {
        "text": "88879898",
        "region_id": 20
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

#           Test_Api_6 Поиск по категориям
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Поиск по категориям")
@allure.description("Получаем товар через вкладку с категориями товаров") 
@allure.feature('Test_Api_6')
def test_by_category():
    with allure.step("6. Запрос:" "Поиск по категориям"):
        payload = {
        "text": "Кофе",
        "region_id": 20
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

#           Test_Api_7 Поиск по частичному совпадению
@allure.epic("Market-Delivery")
@allure.severity (severity_level='normal') 
@allure.title("Поиск по частичному совпадению")
@allure.description("Получаем товар по частичному совпадению") 
@allure.feature('Test_Api_7')
def test_partial_match():
    with allure.step("7. Запрос:" "Поиск по частичному совпадению"):
        payload = {
        "text": "Пицц",
        "region_id": 20
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

if __name__ == "__main__":
    pytest.main()