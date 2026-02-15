from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class RadioButtonsPage(BasePage):

    BLUE_RADIO = (By.ID, "blue")
    TENNIS_RADIO = (By.ID, "tennis")

    def go_to_radio_page(self):
        self.visit("https://practice.expandtesting.com/radio-buttons")

    def select_blue_color(self):
        self.click(self.BLUE_RADIO)

    def select_tennis_sport(self):
        self.click(self.TENNIS_RADIO)

    def is_blue_selected(self):
        return self.find(self.BLUE_RADIO).is_selected()

    def is_tennis_selected(self):
        return self.find(self.TENNIS_RADIO).is_selected()
