from pages.AuthPage import AuthPage

def first_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("andriyas@mail.ru", "Andriyas_011280")

