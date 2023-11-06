from selenium import webdriver

from config.config_ui import BASE_URL
from modules.ui.pages.enrol_page.enroll_page import EnrollPage
from modules.ui.pages.home_page.home_page import HomePage


class EnrollFacade:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.driver.fullscreen_window()
        self.home_page = HomePage(self.driver)
        self.enroll_page = EnrollPage(self.driver)
        self.active_page = self.home_page

    def enroll(self, user_data, message):
        if self.active_page != self.home_page:
            raise RuntimeError("Can't use enroll on page, which is not home_page")
        self.home_page.go_to_enroll()
        self.enroll_page.fill_and_send_form(user_data["first_name"], user_data["last_name"], user_data["email"],
                                            user_data["mobile"], user_data["city"], message)
