""" Локаторы и методы страницы логина пользователя сайта opencart """

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from robot.api.deco import library, keyword


@library("LoginAdminLibrary")
class LoginAdminLibrary:
    """ Локаторы и методы страницы логина пользователя сайта opencart """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    a_browser = webdriver.Chrome()

    admin_login_url = "http://localhost:8888/opencart/admin/"

    login = "admin"
    password = "admin"

    login_panel = (By.CSS_SELECTOR, '.panel-default')
    name_input = (By.CSS_SELECTOR, '#input-username')
    password_input = (By.CSS_SELECTOR, '#input-password')
    admin_login_button = (By.CSS_SELECTOR, 'button.btn')
    admin_logout_button = (By.CLASS_NAME, 'fa-sign-out')

    close_security_alert_button = (By.CSS_SELECTOR, ".close")

    # @keyword("Перейти на страницу авторизации admin")
    def go_to_admin_login_page(self):
        """ Метод перехода на страницу admin login администраторской части opencart """

        self.browser.get(self.admin_login_url)

    # @keyword("Ввести логин и пароль")
    def enter_admin_login_and_password(self, login=login, password=password):
        """ Ввод логина и пароля в админской части магазина opencart """

        self.browser.find_element(*self.name_input).send_keys(login)
        self.browser.find_element(*self.password_input).send_keys(password)

    # @keyword("Кликнуть на кнопку авторизации")
    def click_admin_login_button(self):
        """ Авторизация в админской части магазина opencart """

        self.browser.find_element(*self.submit_button).click()

    # @keyword("Закрыть предупреждающее окно")
    def close_security_alert(self):
        """ Закрытие предупреждающего окна при загрузке страницы """

        self.browser.find_element(*self.close_security_alert_button).click()

    # @keyword("Дождаться присутствия элемента:")
    def wait_admin_element_present(self, locator):
        """ Метод ожидания появления элемента """

        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.presence_of_all_elements_located(locator))
