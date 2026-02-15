from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def go_to_login(self):
        self.visit("https://practice.expandtesting.com/login")

    def enter_username(self, username):
        self.type(self.USERNAME, username)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BTN)
