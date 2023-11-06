from modules.ui.pages.base_page import BasePage
from modules.ui.pages.home_page.home_locators import home_page_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = home_page_locators

    def go_to_enroll(self):
        self.enroll_btn.click()
