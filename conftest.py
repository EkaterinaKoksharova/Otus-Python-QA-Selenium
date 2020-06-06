"""  Фикстуры тестов сайта opencart """

import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


def pytest_addoption(parser):
    """  Параметры, передаваемые в командную строку при запуске тестов """

    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome, firefox, safari or remote, "
                          "remote_standalone, remote_browserstack or remote selenoid")
    parser.addoption("--url",
                     default="http://localhost:8080/opencart/",
                     help="This is request url")
    parser.addoption("--wait",
                     default=10,
                     help="This is time parameter for driver wait")
    parser.addoption("--implicitly_wait",
                     default=1,
                     help="This is time parameter for driver implicitly wait")
    parser.addoption("--log_file",
                     default=None,
                     help="This is a file adress, where selenium logs will be")
    parser.addoption("--log_level",
                     default="INFO",
                     help="This is a log level parameter")
    parser.addoption("--remote_browser", action="store", default="chrome",
                     choices=["chrome", "firefox", "opera", "yandex"],
                     help="This is a remote browser type")
    parser.addoption("--executor", action="store", default="10.0.2.15",
                     help="This is ip for browser.Remote executor")


class MyListener(AbstractEventListener):
    """ Класс с методами логирования действия драйвера """

    def __init__(self, request):
        logging.basicConfig(filename=request.config.getoption("log_file"),
                            level=request.config.getoption("log_level"))

    def after_navigate_to(self, url, driver):
        logging.info('Driver navigated on %s', url)

    def after_find(self, by, value, driver):
        logging.info('Driver found %s with %s', value, by)

    def after_click(self, element, driver):
        logging.info('Driver clicked on %s', element)

    def after_execute_script(self, script, driver):
        logging.info('Driver executed %s', script)

    def after_quit(self, driver):
        logging.info('Driver quit')

    def on_exception(self, exception, driver):
        logging.error('Exception: %s', exception)
        driver.get_screenshot_as_file(f'logs/{exception}.png')


@pytest.fixture(scope="function")
def browser(request):
    """ Значение параметра --browser_name, переданного в команде pytest """

    logging.info('====Browser Fixture Started====')

    browser_name = request.config.getoption("--browser_name")
    remote_browser = request.config.getoption("--remote_browser")
    executor = request.config.getoption("--executor")
    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--window-size=1920x1080")
        options.add_experimental_option('w3c', False)
        DesiredCapabilities.CHROME['loggingPrefs'] = {'browser': 'ALL', 'driver': 'ALL'}
        driver = EventFiringWebDriver\
            (webdriver.Chrome(desired_capabilities=DesiredCapabilities.CHROME,
                              options=options),
             MyListener(request))
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        options.add_argument("--window-size=1920x1080")
        driver = EventFiringWebDriver(webdriver.Firefox(options=options), MyListener(request))
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "remote_standalone":
        driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                  desired_capabilities={"browserName": remote_browser})
    elif browser_name == "remote_browserstack":
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '50.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Opencart Otus QA',
            'browserstack.local': 'true'
        }
        driver = webdriver.Remote(
            command_executor='https://bsuser63897:sEzEdkTCAsz4ZLuakvgk@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)
    elif browser_name == "remote_selenoid":
        capabilities = {
            'browserName': 'chrome',
            'version': '70.0',
            'enableVNC': True,
            'enableVideo': False,
            'enableLog': False}
        driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                  desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--browser_name should be chrome, "
                                "firefox, safari, remote_standalone, "
                                "remote_browserstack or remote selenoid")

    implicitly_wait_parameter = request.config.getoption('--implicitly_wait')
    driver.implicitly_wait(implicitly_wait_parameter)

    yield driver
    driver.quit()

    logging.info('====Browser Fixture Finished====')


@pytest.fixture(scope="function")
def wait(browser, request):
    """ Значение параметра --wait, переданного в команде pytest """

    wait_parameter = request.config.getoption('--wait')
    return WebDriverWait(browser, wait_parameter)


@pytest.fixture(scope="function")
def url(request):
    """ Значение параметра --url, переданного в команде pytest """

    return request.config.getoption('--url')
