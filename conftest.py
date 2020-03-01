"""  Фикстуры тестов сайта opencart """

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """  Параметры, передаваемые в командную строку при запуске тестов """

    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome, firefox or safari")
    parser.addoption("--url",
                     default="http://localhost:8080/opencart/",
                     help="This is request url")


@pytest.fixture(scope="function")
def url(request):
    """ Значение параметра --url, переданного в команде pytest """

    return request.config.getoption('--url')


@pytest.fixture(scope="function")
def browser(request):
    """ Значение параметра --browser_name, переданного в команде pytest """

    browser_name = request.config.getoption("browser_name")
    print(browser_name)
    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("headless")
        options.add_argument("--window-size=1920x1080")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or safari")
    yield driver
    driver.quit()
