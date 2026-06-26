from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AuthPage(BasePage):
    URL = "https://b2c.passport.rt.ru/"

    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")
    FIELD_USERNAME = (By.ID, "username")
    FIELD_PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "kc-login")
    LINK_REGISTER = (By.ID, "kc-register")
    LINK_FORGOT = (By.ID, "forgot_password")
    ERROR_MESSAGE = (By.ID, "form-error-message")
    SOCIAL_VK = (By.ID, "oidc_vk")
    SOCIAL_OK = (By.ID, "oidc_ok")
    PAGE_TITLE = (By.ID, "card-title")

    def open(self):
        self.driver.get(self.URL)

    def click_tab_phone(self):
        self.find_clickable(*self.TAB_PHONE).click()

    def click_tab_email(self):
        self.find_clickable(*self.TAB_EMAIL).click()

    def click_tab_login(self):
        self.find_clickable(*self.TAB_LOGIN).click()

    def click_tab_ls(self):
        self.find_clickable(*self.TAB_LS).click()

    def enter_username(self, value):
        field = self.find_element(*self.FIELD_USERNAME)
        field.clear()
        field.send_keys(value)

    def enter_password(self, value):
        field = self.find_element(*self.FIELD_PASSWORD)
        field.clear()
        field.send_keys(value)

    def click_login(self):
        self.find_clickable(*self.BTN_LOGIN).click()

    def click_register(self):
        self.find_clickable(*self.LINK_REGISTER).click()

    def click_forgot_password(self):
        self.find_clickable(*self.LINK_FORGOT).click()

    def get_error_message(self):
        return self.find_element(*self.ERROR_MESSAGE).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()