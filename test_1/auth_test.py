import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage

def auth_test(browser):
    email = "andriyas80@gmail.com"
    password = "Andriyas_80"
    username = "Андрей Андрияс"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL"+ current_url+ "заканчивается на andrew_011280/boards"):
        assert current_url.endswith("andrew_011280/boards")
        
    with allure.step("Проверить, что указаны данные пользователя"):    
        with allure.step("Имя пользователя должно быть"+username):
            assert info[0] == username 
        with allure.step("Почта пользователя должна быть"+email):
            assert info[1] == email


