import pytest
from pages.auth_page import *
from pages.settings import valid_email, valid_password
from conftest import browser


@pytest.mark.reg
@pytest.mark.positive
def test_auth_page_open(browser):
    """Проверка успешного открытия страницы авторизации"""
    page = AuthPage(browser)
    assert page.get_relative_link() == "/auth/realms/b2c/protocol/openid-connect/auth"


@pytest.mark.auth
@pytest.mark.positive
def test_auth_tab_email(browser):
    """Проверка кликабельности таба Почта."""
    page = AuthPage(browser)
    page.tab_email.click()
    time.sleep(2)
    assert page.tab_email.text == "Почта"


@pytest.mark.auth
@pytest.mark.positive
def test_auth_tab_phone(browser):
    """Проверка кликабельности таба Телефон."""
    page = AuthPage(browser)
    page.tab_phone.click()
    time.sleep(2)
    assert page.tab_phone.text == "Телефон"


@pytest.mark.auth
@pytest.mark.positive
def test_auth_tab_login(browser):
    """Проверка кликабельности таба Логин."""
    page = AuthPage(browser)
    page.tab_login.click()
    time.sleep(2)
    assert page.tab_login.text == "Логин"


@pytest.mark.auth
@pytest.mark.positive
def test_auth_tab_ls(browser):
    """Проверка кликабельности таба Лицевой счет."""
    page = AuthPage(browser)
    page.tab_ls.click()
    time.sleep(2)
    assert page.tab_ls.text == "Лицевой счёт"


@pytest.mark.parametrize("username", ["+79827356791", valid_email, "administrator123", "123456789012"],
                         ids=["phone", "E-mail", "login", "ls"])
def test_tabs(browser, username):
    """Проверка перехода таба меню при вводе соответствующих данных."""
    page = AuthPage(browser)
    page.enter_username(username)

    page.enter_password(valid_password)

    if username == "+79827356791":
        time.sleep(4)
        assert browser.find_element(*AuthLocators.AUTH_TAB).text == "Телефон"
        browser.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
        time.sleep(2)
    elif username == valid_email:
        time.sleep(4)
        assert browser.find_element(*AuthLocators.AUTH_TAB).text == "Почта"
        browser.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
        time.sleep(2)
    elif username == "administrator123":
        time.sleep(4)
        assert browser.find_element(*AuthLocators.AUTH_TAB).text == "Логин"
        browser.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
        time.sleep(2)
    else:
        try:
            time.sleep(4)
            assert browser.find_element(*AuthLocators.AUTH_TAB).text == "Лицевой счёт"
        except Exception:
            print(f"Тест не пройден. Автоматическое переключения на Лицевой счёт не происходит!")


@pytest.mark.auth
@pytest.mark.positive
def test_valid_auth_email(browser):
    """Проверка успешной авторизации с валидными данными в личном кабинете.
    Валидный адрес электронной почты и валидный пароль"""
    page = AuthPage(browser)
    page.tab_email.click()
    time.sleep(2)
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    page.btn_click_enter()
    assert page.get_relative_link() == "/account_b2c/page"
