from pages.auth_page import *
from pages.settings import *
from conftest import browser


def test_auth_page_invalid_email(browser):
    """Негативный сценарий авторизации в личном кабинете по адресу электронной почты.
    Невалидный адрес электронной почты."""
    page = AuthPage(browser)
    page.enter_username(random_email)  # вводим невалидный адрес электронной почты
    page.enter_password(valid_password)  # вводим валидный пароль
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или пароль"


def test_auth_page_invalid_password(browser):
    """Негативный сценарий авторизации в личном кабинете по адресу электронной почты.
    Невалидный пароль."""
    page = AuthPage(browser)
    page.enter_username(valid_email)  # вводим валидный адрес электронной почты
    page.enter_password(random_password)  # вводим невалидный пароль
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или пароль"
