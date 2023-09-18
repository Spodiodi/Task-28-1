import pytest
from pages.auth_page import *
from pages.settings import *
import time
from conftest import browser


@pytest.mark.reg
@pytest.mark.negatvie
def test_get_registration_pass_diff_pass_conf(browser):
    """Негативный сценарий регистрации в личном кабинете.
    Значения в полях ввода 'Пароль' и 'Подтверждение пароля' не совпадают."""
    page = AuthPage(browser)   # нажимаем на гиперссылку "Зарегистрироваться"
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)
    page.enter_firstname(valid_firstname)   # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(valid_lastname)   # вводим валидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(valid_email)   # вводим валидный адрес электронной почты
    browser.implicitly_wait(3)

    page.enter_password(valid_password)   # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(random_password)   # вводим невалидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()   # нажимаем на кнопку "Зарегистрироваться"
    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)
    time.sleep(5)

    assert error_mess.text == "Пароли не совпадают"


@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("phone", ["", 1, 3333333333, generate_string_rus(11), english_chars(), special_chars()],
                         ids=['empty line', 'one digit', '10_digits', 'string_rus', 'english_chars', 'special_chars'])
def test_get_registration_invalid_format_phone(browser, phone):
    """Негативный сценарий регистрации в личном кабинете.
    Невалидный формат номера телефона.
    Применена техника выделения классов эквивалентности и анализа граничных значений."""
    page = AuthPage(browser)
    page.enter_reg_page()  # нажимаем на гиперссылку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)

    page.enter_firstname(valid_firstname)  # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(valid_lastname)  # вводим валидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(phone)  # вводим невалидный номер мобильного телефона
    browser.implicitly_wait(3)

    page.enter_password(valid_password)  # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(valid_password)  # вводим валидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()  # нажимаем на кнопку "Зарегистрироваться"

    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)
    assert error_mess.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, " \
                              "или email в формате example@email.ru"


@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("firstname", ["", generate_string_rus(1), generate_string_rus(31), generate_string_rus(256),
                                       english_chars(), special_chars(), 53519, chinese_symbols()],
                         ids=['empty line', 'one char', 'chars', '256 chars', 'english',
                              'special', 'number', 'chinese_symbols'])
def test_get_registration_invalid_format_firstname(browser, firstname):
    """Негативный сценарий регистрации в личном кабинете.
    Невалидный формат Имени."""
    page = AuthPage(browser)
    page.enter_reg_page()  # нажимаем на гиперссылку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)
    page.enter_firstname(firstname)  # вводим невалидное имя
    browser.implicitly_wait(2)

    page.enter_lastname(valid_lastname)  # вводим валидную фамилию
    browser.implicitly_wait(2)

    page.enter_email(valid_email)  # вводим валидный адрес эл. почты
    browser.implicitly_wait(2)

    page.enter_password(valid_password)  # вводим валидый пароль
    browser.implicitly_wait(2)

    page.enter_pass_conf(valid_password)  # вводим валидное подтверждение пароля
    browser.implicitly_wait(2)

    page.btn_click()  # нажимаем на кнопку "Зарегистрироваться"
    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)

    assert error_mess.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("lastname", ["", generate_string_rus(1), generate_string_rus(31), generate_string_rus(256),
                                      english_chars(), special_chars(), 75435, chinese_symbols()],
                         ids=['empty line', 'one char', '31 chars', '256 chars', 'english', 'special',
                              'number', 'chinese_symbols'])
def test_get_registration_invalid_format_lastname(browser, lastname):
    """Негативный сценарий регистрации в личном кабинете.
    Невалидный формат Фамилии."""
    page = AuthPage(browser)
    page.enter_reg_page()  # нажимаем на гиперссылку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)

    page.enter_firstname(valid_firstname)  # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(lastname)  # вводим невалидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(valid_email)  # вводим валидный адрес электронной почты
    browser.implicitly_wait(3)

    page.enter_password(valid_password)  # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(valid_password)  # вводим валидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()  # нажимаем на кнопку "Зарегистрироваться"
    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)

    assert error_mess.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("email", ["", "@", "@.", ".", generate_string_rus(20), f"{russian_chars()}@mail.ru", 88888],
                         ids=['empty line', 'at', 'at point', 'point', 'string', 'russian', 'digits'])
def test_get_registration_invalid_format_email(browser, email):
    """Негативный сценарий регистрации в личном кабинете.
    Невалидный формат адреса электронной почты."""
    page = AuthPage(browser)
    page.enter_reg_page()   # нажимаем на гиперссылку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)
    page.enter_firstname(valid_firstname)   # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(valid_lastname)   # вводим валидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(email)   # вводим невалидный адрес электронный почты
    browser.implicitly_wait(3)

    page.enter_password(valid_password)   # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(valid_password)   # вводим валидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()   # нажимаем на кнопку "Зарегистрироваться"
    error_mess = browser.find_element(*AuthLocators.AUTH_MESSAGE_ERROR)

    assert error_mess.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, " \
                              "или email в формате example@email.ru"


@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize("living_email", [valid_email], ids=["living email"])
def test_get_registration_living_account(browser, living_email):
    """Негативный сценарий регистрации в личном кабинете.
    Используется уже зарегистрированный в системе адрес электронной почты."""
    page = AuthPage(browser)
    page.enter_reg_page()   # нажимаем на гиперссылку "Зарегистрироваться"
    browser.implicitly_wait(2)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"

    page = RegPage(browser)
    page.enter_firstname(valid_firstname)   # вводим валидное имя
    browser.implicitly_wait(5)

    page.enter_lastname(valid_lastname)   # вводим валидную фамилию
    browser.implicitly_wait(5)

    page.enter_email(living_email)   # вводим зарегистрированный в системе адрес электронной почты
    browser.implicitly_wait(3)

    page.enter_password(valid_password)   # вводим валидный пароль
    browser.implicitly_wait(3)

    page.enter_pass_conf(valid_password)   # вводим валидное подтверждение пароля
    browser.implicitly_wait(3)

    page.btn_click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(2)
    card_modal_title = browser.find_element(*RegLocators.REG_CARD_MODAL)

    assert card_modal_title.text == "Учётная запись уже существует"
