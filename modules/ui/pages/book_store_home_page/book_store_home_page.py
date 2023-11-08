from modules.ui.pages.base_page import BasePage
from modules.ui.pages.book_store_home_page.book_store_home_locators import book_store_home_page_locators


class BookStoreHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = book_store_home_page_locators

    def go_to_login_form(self):
        self.login_btn.click()

    def pick_book_by_name(self, book_name):
        book_locator_formatter = self.locators["book_name_formatter"]
        self.locators["book_name_btn"] = (
            book_locator_formatter[0].replace("_f", ""), book_locator_formatter[1].format(name=book_name))
        self.book_name_btn.click()
