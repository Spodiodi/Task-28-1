import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    """Создаем экземпляр класса webdriver.
    Инициализируем браузер, останавливаем выполнение функции, ждём окончания теста/тестов.
    Закрываем браузер."""
    print("\nBrowser is started")
    driver = webdriver.Chrome()  # инициализируем браузер
    driver.maximize_window()
    yield driver
    print("\nQuit. Bye.")
    driver.quit()  # закрываем браузер
