import time
from Pages.base_page import BasePage


class InfiniteScrollPage(BasePage):

    def go_to_page(self):
        self.visit("https://practice.expandtesting.com/infinite-scroll")

    def scroll_down_steps(self, steps=8, pause=1):
        for _ in range(steps):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(pause)

    def scroll_to_bottom_smart(self, max_rounds=15):
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight"
        )

        for _ in range(max_rounds):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(1)

            new_height = self.driver.execute_script(
                "return document.body.scrollHeight"
            )

            if new_height == last_height:
                break
            last_height = new_height
