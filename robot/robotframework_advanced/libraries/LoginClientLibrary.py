""" Локаторы и методы страницы логина администратора сайта opencart """

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from robot.api.deco import library, keyword


# @library("LoginClientLibrary")
class LoginClientLibrary:
    """ Локаторы и методы страницы логина администратора сайта opencart """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    browser = webdriver.Chrome()

    client_login_url = "http://localhost:8888/opencart/index.php?route=account/login"

    email = "koksharova3093@gmail.com"
    password = "merterbok"

    email_input = (By.CSS_SELECTOR, '##input-email')
    password_input = (By.CSS_SELECTOR, '#input-password')
    login_button = (By.CSS_SELECTOR, '[value="Login"]')

    client_logout_button = (By.LINK_TEXT, 'Logout')

    # @keyword("Перейти на страницу авторизации client")
    def go_to_client_login_page(self):
        """ Метод перехода на страницу client login клиентской части opencart """

        self.browser.get(self.client_login_url)

    # @keyword("Ввести логин и пароль")
    def enter_client_login_and_password(self, login=login, password=password):
        """ Ввод логина и пароля в клиентской части магазина opencart """

        self.browser.find_element(*self.email_input).send_keys(login)
        self.browser.find_element(*self.password_input).send_keys(password)

    # @keyword("Кликнуть на кнопку авторизации")
    def click_client_login_button(self):
        """ Авторизация в клиентской части магазина opencart """

        self.browser.find_element(*self.login_button).click()

    # @keyword("Дождаться присутствия элемента:")
    def wait_client_element_present(self, locator):
        """ Метод ожидания появления элемента """

        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.presence_of_all_elements_located(locator))
