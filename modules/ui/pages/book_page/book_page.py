from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait

from modules.ui.pages.base_page import BasePage
from modules.ui.pages.book_page.book_locators import book_locators
from selenium.webdriver.support import expected_conditions as EC


class BookPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = book_locators

    def add_book(self):
        self.driver.fullscreen_window()
        self.scroll_site_down()
        self.add_book_btn.click()
        self.driver.fullscreen_window()
        self.scroll_site_down()
        self.profile_menu_btn.click()
        wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
