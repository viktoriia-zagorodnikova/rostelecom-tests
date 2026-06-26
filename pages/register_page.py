from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    URL = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration"

    FIELD_FIRSTNAME = (By.NAME, "firstName")
    FIELD_LASTNAME = (By.NAME, "lastName")
    FIELD_EMAIL = (By.ID, "address")
    FIELD_PASSWORD = (By.ID, "password")
    FIELD_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    BTN_REGISTER = (By.NAME, "register")
    ERROR_FIRSTNAME = (By.CSS_SELECTOR, "#page-right .rt-input-container--error #firstName + .rt-input-container__meta--error")
    ERROR_PASSWORD = (By.CSS_SELECTOR, ".new-password-container .rt-input-container__meta--error")
    ERROR_CONFIRM = (By.CSS_SELECTOR, "#password-confirm ~ .rt-input-container__meta--error")

    def enter_firstname(self, value):
        field = self.find_element(*self.FIELD_FIRSTNAME)
        field.clear()
        field.send_keys(value)

    def enter_lastname(self, value):
        field = self.find_element(*self.FIELD_LASTNAME)
        field.clear()
        field.send_keys(value)

    def enter_email(self, value):
        field = self.find_element(*self.FIELD_EMAIL)
        field.clear()
        field.send_keys(value)

    def enter_password(self, value):
        field = self.find_element(*self.FIELD_PASSWORD)
        field.clear()
        field.send_keys(value)

    def enter_password_confirm(self, value):
        field = self.find_element(*self.FIELD_PASSWORD_CONFIRM)
        field.clear()
        field.send_keys(value)

    def click_register(self):
        self.find_clickable(*self.BTN_REGISTER).click()
