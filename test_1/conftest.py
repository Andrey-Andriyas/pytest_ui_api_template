import allure
import pytest
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api.BoardApi import BoardApi

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "649645d1a6fe75a20b0abb51/ATTSlb59HBDZIAuCK37aVV9JnNnjcdNFDMoNcZzPSk8BUJFaxCORoASi9Vl22jb2BusMA2B73951")

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "")

@pytest.fixture
def dummy_board_id() -> str:
    api = BoardApi("https://api.trello.com/1", "649645d1a6fe75a20b0abb51/ATTSlb59HBDZIAuCK37aVV9JnNnjcdNFDMoNcZzPSk8BUJFaxCORoASi9Vl22jb2BusMA2B73951")
    resp = api.create_board("Board to be deleted").get("id")
    return resp

@pytest.fixture
def delete_board() -> str:
    dictionary = {"board_id" : ""}
    yield dictionary

    api = BoardApi("https://api.trello.com/1", "649645d1a6fe75a20b0abb51/ATTSlb59HBDZIAuCK37aVV9JnNnjcdNFDMoNcZzPSk8BUJFaxCORoASi9Vl22jb2BusMA2B73951")
    api.delete_board_by_id(dictionary.get("board_id"))



