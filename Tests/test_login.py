from Pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login()

    login_page.enter_username("practice")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()
