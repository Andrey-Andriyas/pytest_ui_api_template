from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://trello.com/login"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)
    
    # Пример от Димы Еремина (не сработал, медленно прогружается сайт)
    # def login_as(self, email: str, password: str):
    #     self.__driver.find_element(By.CSS_SELECTOR, "#user").send_keys(email)
    #     self.__driver.find_element(By.CSS_SELECTOR, "#login").click()
    #     self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    #     self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()




    def login_as(self, email: str, password: str):
        email_input = WebDriverWait(self.__driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#user"))
)
        email_input.send_keys(email)
    
        login_button = WebDriverWait(self.__driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#login"))
)
        login_button.click()
    
        password_input = WebDriverWait(self.__driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))
)
        password_input.send_keys(password)
    
        submit_button = WebDriverWait(self.__driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-submit"))
)
        submit_button.click()

    