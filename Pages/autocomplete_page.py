from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage


class AutocompletePage(BasePage):

    COUNTRY_INPUT = (By.ID, "country")
    SUBMIT_BTN = (By.XPATH, "//button[contains(.,'Submit')]")
    RESULT = (By.ID, "result")

    def go_to_page(self):
        self.visit("https://practice.expandtesting.com/autocomplete")

    def select_country(self, name):
        field = self.find(self.COUNTRY_INPUT)
        field.send_keys(name)

        # choose first suggestion via keyboard (more reliable)
        field.send_keys(Keys.ARROW_DOWN)
        field.send_keys(Keys.ENTER)

    def submit_form(self):
        try:
            self.click(self.SUBMIT_BTN)
        except:
            self.js_click(self.SUBMIT_BTN)

    def get_result(self):
        return self.find(self.RESULT).text
