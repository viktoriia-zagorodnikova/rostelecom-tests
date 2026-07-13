import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage

load_dotenv()

VALID_EMAIL = os.environ.get("VALID_EMAIL")
VALID_PASSWORD = os.environ.get("VALID_PASSWORD")
INVALID_PASSWORD = "wrongpassword123"


def test_tk001_auth_page_opens(browser):
    """TC-001: The authorization page opens correctly"""
    page = AuthPage(browser)
    page.open()
    assert "b2c.passport.rt.ru" in page.get_current_url()


def test_tk002_auth_form_title(browser):
    """TC-002: The authorization form title is displayed"""
    page = AuthPage(browser)
    page.open()
    title = page.find_element(By.ID, "card-title")
    assert title.is_displayed()
    # Checking a fragment of the real page text (site UI is in Russian)
    assert "вторизация" in title.text


def test_tk003_tabs_present(browser):
    """TC-003: All 4 authorization tabs are present"""
    page = AuthPage(browser)
    page.open()
    assert page.find_element(*AuthPage.TAB_PHONE).is_displayed()
    assert page.find_element(*AuthPage.TAB_EMAIL).is_displayed()
    assert page.find_element(*AuthPage.TAB_LOGIN).is_displayed()
    assert page.find_element(*AuthPage.TAB_LS).is_displayed()


def test_tk004_tab_phone_active_by_default(browser):
    """TC-004: The 'Phone' tab is active by default"""
    page = AuthPage(browser)
    page.open()
    tab = page.find_element(*AuthPage.TAB_PHONE)
    assert "active" in tab.get_attribute("class")


def test_tk005_tab_email_click(browser):
    """TC-005: The 'Email' tab switches on click"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_email()
    tab = page.find_element(*AuthPage.TAB_EMAIL)
    assert "active" in tab.get_attribute("class")


def test_tk006_tab_login_click(browser):
    """TC-006: The 'Login' tab switches on click"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_login()
    tab = page.find_element(*AuthPage.TAB_LOGIN)
    assert "active" in tab.get_attribute("class")


def test_tk007_tab_ls_click(browser):
    """TC-007: The 'Account Number' tab switches on click"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_ls()
    tab = page.find_element(*AuthPage.TAB_LS)
    assert "active" in tab.get_attribute("class")


def test_tk008_username_field_present(browser):
    """TC-008: The username input field is present"""
    page = AuthPage(browser)
    page.open()
    field = page.find_element(*AuthPage.FIELD_USERNAME)
    assert field.is_displayed()


def test_tk009_password_field_present(browser):
    """TC-009: The password input field is present"""
    page = AuthPage(browser)
    page.open()
    field = page.find_element(*AuthPage.FIELD_PASSWORD)
    assert field.is_displayed()


def test_tk010_login_button_present(browser):
    """TC-010: The 'Login' button is present"""
    page = AuthPage(browser)
    page.open()
    btn = page.find_element(*AuthPage.BTN_LOGIN)
    assert btn.is_displayed()


def test_tk011_register_link_present(browser):
    """TC-011: The 'Sign up' link is present"""
    page = AuthPage(browser)
    page.open()
    link = page.find_element(*AuthPage.LINK_REGISTER)
    assert link.is_displayed()


def test_tk012_forgot_password_link_present(browser):
    """TC-012: The 'Forgot password' link is present"""
    page = AuthPage(browser)
    page.open()
    link = page.find_element(*AuthPage.LINK_FORGOT)
    assert link.is_displayed()


def test_tk013_register_link_redirects(browser):
    """TC-013: Clicking 'Sign up' opens the registration form"""
    page = AuthPage(browser)
    page.open()
    page.click_register()
    WebDriverWait(browser, 10).until(EC.url_contains("registration"))
    assert "registration" in page.get_current_url()


def test_tk014_forgot_password_redirects(browser):
    """TC-014: Clicking 'Forgot password' opens the recovery form"""
    page = AuthPage(browser)
    page.open()
    page.click_forgot_password()
    WebDriverWait(browser, 10).until(
        lambda d: d.current_url != "https://b2c.passport.rt.ru/"
    )
    assert page.get_current_url() != "https://b2c.passport.rt.ru/"


def test_tk015_wrong_password_shows_error(browser):
    """TC-015: Logging in with an incorrect password shows an error"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_email()
    page.enter_username(VALID_EMAIL)
    page.enter_password(INVALID_PASSWORD)
    page.click_login()
    error = page.find_element(By.ID, "form-error-message")
    assert error.is_displayed()


def test_tk016_username_field_accepts_input(browser):
    """TC-016: The username field accepts text input"""
    page = AuthPage(browser)
    page.open()
    page.enter_username("test@example.com")
    field = page.find_element(*AuthPage.FIELD_USERNAME)
    assert field.get_attribute("value") == "test@example.com"


def test_tk017_social_buttons_present(browser):
    """TC-017: Social login buttons are present"""
    page = AuthPage(browser)
    page.open()
    vk = page.find_element(*AuthPage.SOCIAL_VK)
    ok = page.find_element(*AuthPage.SOCIAL_OK)
    assert vk.is_displayed()
    assert ok.is_displayed()


def test_tk018_tab_email_shows_email_field(browser):
    """TC-018: Selecting the 'Email' tab updates the field placeholder"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_email()
    field = page.find_element(*AuthPage.FIELD_USERNAME)
    placeholder = field.get_attribute("placeholder")
    assert placeholder is not None


def test_tk019_successful_login(browser):
    """TC-019: Successful login with email and password"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_email()
    page.login(VALID_EMAIL, VALID_PASSWORD)
    WebDriverWait(browser, 15).until(
        lambda d: "b2c.passport.rt.ru/login" not in d.current_url
    )
    assert "b2c.passport.rt.ru/login" not in page.get_current_url()


def test_tk020_tab_phone_shows_phone_field(browser):
    """TC-020: Selecting the 'Phone' tab displays the phone field"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_phone()
    field = page.find_element(*AuthPage.FIELD_USERNAME)
    assert field.is_displayed()
