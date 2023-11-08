import time

from modules.ui.pages.base_page import BasePage
from modules.ui.pages.profile_page.profile_locators import profile_locators


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = profile_locators

    def go_to_home_bookstore(self):
        self.book_store_menu_btn.click()

    def validate_book_name_in_list(self, book_name):
        book_locator_formatter = self.locators["book_name_formatter"]
        self.locators["book_name_btn"] = (
            book_locator_formatter[0].replace("_f", ""), book_locator_formatter[1].format(name=book_name))
        time.sleep(10)
        assert self.book_name_btn

    def delete_account(self):
        self.driver.fullscreen_window()
        self.delete_account_btn.click()
