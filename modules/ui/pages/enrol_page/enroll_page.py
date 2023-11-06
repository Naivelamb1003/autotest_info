import time

from modules.ui.pages.base_page import BasePage
from modules.ui.pages.enrol_page.enroll_locators import enroll_page_locators


class EnrollPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = enroll_page_locators

    def fill_and_send_form(self, first_name, last_name, email, mobile, city, message):
        self.first_name_inp.send_keys(first_name)
        self.last_name_inp.send_keys(last_name)
        self.email_inp.send_keys(email)
        self.mobile_inp.send_keys(mobile)
        self.country_inp.click()
        self.country_option.click()
        self.city_inp.send_keys(city)
        self.message_inp.send_keys(message)
        print("please solve the captcha")
        time.sleep(30)
        self.send_btn.click()

