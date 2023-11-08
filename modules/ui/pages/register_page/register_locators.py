register_locators = {
    "firstname_inp": ("ID", "firstname"),
    "lastname_inp": ("ID", "lastname"),
    "username_inp": ("ID", "userName"),
    "password_inp": ("ID", "password"),
    "captcha_iframe": ("XPATH", "//iframe[contains(@title, 'reCAPTCHA')]"),
    "captcha": ("XPATH", "//span[@id='recaptcha-anchor']"),
    "checked_captcha": ("CLASS_NAME", "recaptcha-checkbox-checked"),
    "register_btn": ("ID", "register"),
    "go_to_login_btn": ("ID", "gotologin"),
}
