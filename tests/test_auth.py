import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage

VALID_EMAIL = "doorgaliyo@gmail.com"
VALID_PASSWORD = "-ZQVigas5YYiH!9"
INVALID_PASSWORD = "wrongpassword123"


def test_tk001_auth_page_opens(browser):
    """ТК-001: Страница авторизации открывается корректно"""
    page = AuthPage(browser)
    page.open()
    assert "b2c.passport.rt.ru" in page.get_current_url()


def test_tk002_auth_form_title(browser):
    """ТК-002: Заголовок формы авторизации отображается"""
    page = AuthPage(browser)
    page.open()
    title = page.find_element(By.ID, "card-title")
    assert title.is_displayed()
    assert "вторизация" in title.text


def test_tk003_tabs_present(browser):
    """ТК-003: Все 4 таба авторизации присутствуют"""
    page = AuthPage(browser)
    page.open()
    assert page.find_element(*AuthPage.TAB_PHONE).is_displayed()
    assert page.find_element(*AuthPage.TAB_EMAIL).is_displayed()
    assert page.find_element(*AuthPage.TAB_LOGIN).is_displayed()
    assert page.find_element(*AuthPage.TAB_LS).is_displayed()


def test_tk004_tab_phone_active_by_default(browser):
    """ТК-004: Таб 'Телефон' активен по умолчанию"""
    page = AuthPage(browser)
    page.open()
    tab = page.find_element(*AuthPage.TAB_PHONE)
    assert "active" in tab.get_attribute("class")


def test_tk005_tab_email_click(browser):
    """ТК-005: Таб 'Почта' переключается при клике"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_email()
    tab = page.find_element(*AuthPage.TAB_EMAIL)
    assert "active" in tab.get_attribute("class")


def test_tk006_tab_login_click(browser):
    """ТК-006: Таб 'Логин' переключается при клике"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_login()
    tab = page.find_element(*AuthPage.TAB_LOGIN)
    assert "active" in tab.get_attribute("class")


def test_tk007_tab_ls_click(browser):
    """ТК-007: Таб 'Лицевой счёт' переключается при клике"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_ls()
    tab = page.find_element(*AuthPage.TAB_LS)
    assert "active" in tab.get_attribute("class")


def test_tk008_username_field_present(browser):
    """ТК-008: Поле ввода логина присутствует"""
    page = AuthPage(browser)
    page.open()
    field = page.find_element(*AuthPage.FIELD_USERNAME)
    assert field.is_displayed()


def test_tk009_password_field_present(browser):
    """ТК-009: Поле ввода пароля присутствует"""
    page = AuthPage(browser)
    page.open()
    field = page.find_element(*AuthPage.FIELD_PASSWORD)
    assert field.is_displayed()


def test_tk010_login_button_present(browser):
    """ТК-010: Кнопка 'Войти' присутствует"""
    page = AuthPage(browser)
    page.open()
    btn = page.find_element(*AuthPage.BTN_LOGIN)
    assert btn.is_displayed()


def test_tk011_register_link_present(browser):
    """ТК-011: Ссылка 'Зарегистрироваться' присутствует"""
    page = AuthPage(browser)
    page.open()
    link = page.find_element(*AuthPage.LINK_REGISTER)
    assert link.is_displayed()


def test_tk012_forgot_password_link_present(browser):
    """ТК-012: Ссылка 'Забыл пароль' присутствует"""
    page = AuthPage(browser)
    page.open()
    link = page.find_element(*AuthPage.LINK_FORGOT)
    assert link.is_displayed()


def test_tk013_register_link_redirects(browser):
    """ТК-013: Клик на 'Зарегистрироваться' открывает форму регистрации"""
    page = AuthPage(browser)
    page.open()
    page.click_register()
    WebDriverWait(browser, 10).until(EC.url_contains("registration"))
    assert "registration" in page.get_current_url()


def test_tk014_forgot_password_redirects(browser):
    """ТК-014: Клик на 'Забыл пароль' открывает форму восстановления"""
    page = AuthPage(browser)
    page.open()
    page.click_forgot_password()
    WebDriverWait(browser, 10).until(
        lambda d: d.current_url != "https://b2c.passport.rt.ru/"
    )
    assert page.get_current_url() != "https://b2c.passport.rt.ru/"


def test_tk015_wrong_password_shows_error(browser):
    """ТК-015: Вход с неверным паролем показывает ошибку"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_email()
    page.enter_username(VALID_EMAIL)
    page.enter_password(INVALID_PASSWORD)
    page.click_login()
    error = page.find_element(By.ID, "form-error-message")
    assert error.is_displayed()


def test_tk016_username_field_accepts_input(browser):
    """ТК-016: Поле username принимает текст"""
    page = AuthPage(browser)
    page.open()
    page.enter_username("test@example.com")
    field = page.find_element(*AuthPage.FIELD_USERNAME)
    assert field.get_attribute("value") == "test@example.com"


def test_tk017_social_buttons_present(browser):
    """ТК-017: Кнопки входа через соцсети присутствуют"""
    page = AuthPage(browser)
    page.open()
    vk = page.find_element(*AuthPage.SOCIAL_VK)
    ok = page.find_element(*AuthPage.SOCIAL_OK)
    assert vk.is_displayed()
    assert ok.is_displayed()


def test_tk018_tab_email_shows_email_field(browser):
    """ТК-018: При выборе таба 'Почта' поле меняет placeholder"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_email()
    field = page.find_element(*AuthPage.FIELD_USERNAME)
    placeholder = field.get_attribute("placeholder")
    assert placeholder is not None


def test_tk019_successful_login(browser):
    """ТК-019: Успешный вход по email и паролю"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_email()
    page.login(VALID_EMAIL, VALID_PASSWORD)
    WebDriverWait(browser, 15).until(
        lambda d: "b2c.passport.rt.ru/login" not in d.current_url
    )
    assert "b2c.passport.rt.ru/login" not in page.get_current_url()


def test_tk020_tab_phone_shows_phone_field(browser):
    """ТК-020: При выборе таба 'Телефон' отображается поле телефона"""
    page = AuthPage(browser)
    page.open()
    page.click_tab_phone()
    field = page.find_element(*AuthPage.FIELD_USERNAME)
    assert field.is_displayed()