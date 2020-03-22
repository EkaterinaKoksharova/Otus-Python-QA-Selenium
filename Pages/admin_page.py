""" Локаторы и методы страницы логина администратора сайта opencart """

from selenium.webdriver.common.by import By


class AdminPage:
    """ Локаторы и методы страницы логина администратора сайта opencart """

    adm_login_url = "http://localhost:8080/opencart/admin/"

    admin_login = "admin"
    admin_password = "admin"

    login_panel = (By.CSS_SELECTOR, '.panel-default')
    name_input = (By.CSS_SELECTOR, '#input-username')
    password_input = (By.CSS_SELECTOR, '#input-password')
    submit_button = (By.CSS_SELECTOR, 'button.btn')
    forgotten_password_link = (By.CSS_SELECTOR, '.help-block')
    error_message = (By.CSS_SELECTOR, '.alert-dismissible')

    menu_catalogue = (By.CSS_SELECTOR, '#menu-catalog')
    menu_products = (By.CSS_SELECTOR, '#collapse1 > :nth-child(2)')

    @staticmethod
    def admin_login_right(browser):
        """ Авторизация в админской части магазина opencart """

        browser.get(AdminPage.adm_login_url)

        browser.find_element(*AdminPage.name_input).send_keys(AdminPage.admin_login)
        browser.find_element(*AdminPage.password_input).send_keys(AdminPage.admin_password)

        browser.find_element(*AdminPage.submit_button).click()
