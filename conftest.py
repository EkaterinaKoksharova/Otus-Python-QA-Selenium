"""  Фикстуры тестов сайта opencart """

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def pytest_addoption(parser):
    """  Параметры, передаваемые в командную строку при запуске тестов """

    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome, firefox or safari")
    parser.addoption("--url",
                     default="http://localhost:8080/opencart/",
                     help="This is request url")
    parser.addoption("--wait",
                     default=10,
                     help="This is time parameter for driver wait")
    parser.addoption("--implicitly_wait",
                     default=0,
                     help="This is time parameter for driver implicitly wait")


@pytest.fixture(scope="function")
def url(request):
    """ Значение параметра --url, переданного в команде pytest """

    return request.config.getoption('--url')


@pytest.fixture(scope="function")
def browser(request):
    """ Значение параметра --browser_name, переданного в команде pytest """

    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
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

    implicitly_wait_parameter = request.config.getoption('--implicitly_wait')
    driver.implicitly_wait(implicitly_wait_parameter)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(browser, request):
    """ Значение параметра --wait, переданного в команде pytest """

    wait_parameter = request.config.getoption('--wait')
    return WebDriverWait(browser, wait_parameter)
