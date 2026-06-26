from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RecoveryPage(BasePage):
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    FIELD_USERNAME = (By.ID, "username")
    BTN_CONTINUE = (By.ID, "reset")
    BTN_BACK = (By.ID, "reset-back")
    HEADING = (By.CSS_SELECTOR, ".card-container__title")

    def get_heading(self):
        return self.find_element(*self.HEADING).text

    def click_back(self):
        self.find_clickable(*self.BTN_BACK).click()

    def enter_username(self, value):
        field = self.find_element(*self.FIELD_USERNAME)
        field.clear()
        field.send_keys(value)

    def click_continue(self):
        self.find_clickable(*self.BTN_CONTINUE).click()
