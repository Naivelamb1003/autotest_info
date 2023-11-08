from config.config_ui import WAIT_TIME
from modules.ui.pages.base_page import BasePage
from modules.ui.pages.register_page.register_locators import register_locators


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = register_locators
    timeout = WAIT_TIME

    def fill_registration_form(self, first_name, last_name, user_name, password):
        self.firstname_inp.send_keys(first_name)
        self.lastname_inp.send_keys(last_name)
        self.username_inp.send_keys(user_name)
        self.password_inp.send_keys(password)
        self.driver.switch_to.frame(self.captcha_iframe)
        self.captcha.click()
        if not self.checked_captcha:
            raise RuntimeError("Captcha wasn't passed")
        self.driver.switch_to.default_content()
        self.register_btn.click()
        self.dismiss_alert()

    def go_to_login(self):
        self.go_to_login_btn.click()
