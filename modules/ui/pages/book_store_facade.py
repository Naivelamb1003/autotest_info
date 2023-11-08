import time

from selenium import webdriver

from config.config_ui import BASE_URL
from modules.ui.pages.book_page.book_page import BookPage
from modules.ui.pages.book_store_home_page.book_store_home_page import BookStoreHomePage
from modules.ui.pages.home_page.home_page import HomePage
from modules.ui.pages.login_page.login_page import LoginPage
from modules.ui.pages.profile_page.profile_page import ProfilePage
from modules.ui.pages.register_page.register_page import RegistrationPage


class BookStoreFacade:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.driver.fullscreen_window()
        self.home_page = HomePage(self.driver)
        self.book_store_home_page = BookStoreHomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.registration_page = RegistrationPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.book_page = BookPage(self.driver)
        self.active_page = self.home_page

    def register(self, user_data, user_name):
        if self.active_page != self.home_page:
            raise RuntimeError("Can't use registration on page, which is not home_page")
        self.home_page.go_to_book_store()
        self.book_store_home_page.go_to_login_form()
        self.login_page.go_to_registration()
        self.registration_page.fill_registration_form(user_data["first_name"], user_data["last_name"],
                                                      user_name,
                                                      user_data["password"])
        self.active_page = self.registration_page

    def login(self, user_data, user_name):
        if self.active_page != self.registration_page:
            raise RuntimeError("Can't use login on page, which is not registration page")
        self.registration_page.go_to_login()
        self.login_page.fill_form_and_login(user_name, user_data["password"])
        self.active_page = self.profile_page
        time.sleep(2)

    def add_book(self, book_name):
        if self.active_page != self.profile_page:
            raise RuntimeError("Can't add book on page, which is not profile")
        self.profile_page.go_to_home_bookstore()
        self.book_store_home_page.pick_book_by_name(book_name)
        self.book_page.add_book()

    def validate_book_and_delete_account(self, book_name):
        if self.active_page != self.profile_page:
            raise RuntimeError("Can't validate on page, which is not profile")
        self.profile_page.validate_book_name_in_list(book_name)
        self.profile_page.delete_account()

    def close_driver(self):
        self.driver.close()
