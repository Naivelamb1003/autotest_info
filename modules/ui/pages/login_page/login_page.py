from modules.ui.pages.base_page import BasePage
from modules.ui.pages.login_page.login_locators import login_locators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = login_locators

    def go_to_registration(self):
        self.new_user_btn.click()

    def fill_form_and_login(self, username, password):
        self.username_inp.send_keys(username)
        self.password_inp.send_keys(password)
        self.login_btn.click()
