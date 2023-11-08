from config.config_ui import DRIVER_NAME
from modules.ui.common.page_factory.page_factory import PageFactory


def transform_page_factory_locator_to_driver(locator):
    return PageFactory.TYPE_OF_LOCATORS.get(locator[0].lower()), locator[1]


class BasePage(PageFactory):
    DRIVER_NAME = DRIVER_NAME

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def get_element_list_by_locator(self, locator) -> list:
        driver_locator = transform_page_factory_locator_to_driver(locator)
        return self.driver.find_elements(driver_locator[0], driver_locator[1])

    def scroll_site_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def dismiss_alert(self):
        self.driver.execute_script("window.alert = function() {};")
