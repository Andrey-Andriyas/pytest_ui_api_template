from pages.AuthPage import AuthPage
from pages.MainPage import MainPage

def auth_test(browser):
    email = "andriyas80@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "Andriyas_80")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    assert main_page.get_current_url().endswith("andrew_011280/boards")
    assert info[0] == "Андрей Андрияс" 
    assert info[1] == email


