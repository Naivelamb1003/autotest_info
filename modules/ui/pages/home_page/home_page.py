from modules.ui.pages.base_page import BasePage
from modules.ui.pages.home_page.home_locators import home_page_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = home_page_locators

    def go_to_book_store(self):
        self.scroll_site_down()
        menu_btns_locator = home_page_locators["menu_btns"]
        menu_btns = self.get_element_list_by_locator(menu_btns_locator)
        if not menu_btns:
            raise RuntimeError("Can't find locator " + menu_btns_locator)
        menu_btns[-1].click()