""" Локаторы и методы страницы логина администратора сайта opencart """

from selenium.webdriver.common.by import By


class AdminPage:
    """ Локаторы и методы страницы логина администратора сайта opencart """

    admin_login_url = "http://localhost:8080/opencart/admin/"

    admin_login = "admin"
    admin_password = "admin"

    login_panel = (By.CSS_SELECTOR, '.panel-default')
    name_input = (By.CSS_SELECTOR, '#input-username')
    password_input = (By.CSS_SELECTOR, '#input-password')
    submit_button = (By.CSS_SELECTOR, 'button.btn')
    forgotten_password_link = (By.CSS_SELECTOR, '.help-block')
    error_message = (By.CSS_SELECTOR, '.alert-dismissible')

    logout_button = (By.CLASS_NAME, 'fa-sign-out')

    menu_catalogue = (By.CSS_SELECTOR, '#menu-catalog')
    menu_products = (By.CSS_SELECTOR, '#collapse1 > :nth-child(2)')

    alert_danger = (By.CLASS_NAME, 'alert-danger')

    @staticmethod
    def go_to_admin_login_page(browser):
        """ Метод перехода на страницу admin login администраторской части opencart """

        browser.get(AdminPage.admin_login_url)

    @staticmethod
    def login_to_admin(browser, login=admin_login, password=admin_password):
        """ Авторизация в админской части магазина opencart """

        browser.find_element(*AdminPage.name_input).send_keys(login)
        browser.find_element(*AdminPage.password_input).send_keys(password)

        browser.find_element(*AdminPage.submit_button).click()

    @staticmethod
    def logout_from_admin(browser):
        """ Выход из аккаунта в админской части магазина opencart """

        browser.find_element(*AdminPage.logout_button).click()
