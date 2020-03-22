""" Переменные и методы сайта opencart """

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class CommonItems:
    """ Переменные и методы сайта opencart """

    base_url = "http://localhost:8080/opencart/"

    choose_currency = (By.CSS_SELECTOR, "#form-currency")
    choose_currency_euros = (By.CSS_SELECTOR, "[name='EUR']")
    choose_currency_pounds = (By.CSS_SELECTOR, "[name='GPB']")
    choose_currency_dollars = (By.CSS_SELECTOR, "[name='USD']")

    phone = (By.CSS_SELECTOR, ".fa-phone")

    user_menu = (By.CSS_SELECTOR, ".fa-user")
    user_menu_register = (By.CSS_SELECTOR, ".dropdown-menu-right > :nth-child(1)")
    user_menu_login = (By.CSS_SELECTOR, ".dropdown-menu-right > :nth-child(2)")

    wishlist = (By.CSS_SELECTOR, "#wishlist-total")
    shopping_cart = (By.CSS_SELECTOR, "[title='Shopping Cart']")
    checkout = (By.CSS_SELECTOR, "[title='Checkout']")

    logo_button = (By.CSS_SELECTOR, "#logo")
    search_input = (By.CSS_SELECTOR, "#search")
    search_button = (By.CSS_SELECTOR, "#search .btn")
    cart_button = (By.CSS_SELECTOR, "#cart .btn")

    menu = (By.CSS_SELECTOR, "#menu")
    menu_desktops = (By.CSS_SELECTOR, "#menu .nav > :nth-child(1)")
    menu_desktops_see_all = (By.CSS_SELECTOR, "#menu .nav > :nth-child(1) .see-all")

    menu_laptops_and_notebooks = (By.CSS_SELECTOR, "#menu .nav > :nth-child(2)")
    menu_laptops_and_notebooks_see_all = (By.CSS_SELECTOR, "#menu .nav > :nth-child(2) .see-all")

    menu_components = (By.CSS_SELECTOR, "#menu .nav > :nth-child(3)")
    menu_components_see_all = (By.CSS_SELECTOR, "#menu .nav > :nth-child(3) .see-all")

    menu_tablets = (By.CSS_SELECTOR, "#menu .nav > :nth-child(4)")
    menu_software = (By.CSS_SELECTOR, "#menu .nav > :nth-child(5)")
    menu_phones_and_pdas = (By.CSS_SELECTOR, "#menu .nav > :nth-child(6)")
    menu_cameras = (By.CSS_SELECTOR, "#menu .nav > :nth-child(7)")

    menu_mp3_players = (By.CSS_SELECTOR, "#menu .nav > :nth-child(8)")
    menu_mp3_players_see_all = (By.CSS_SELECTOR, "#menu .nav > :nth-child(8) .see-all")

    menu_breadcrumb = (By.CSS_SELECTOR, ".breadcrumb")

    footer = (By.CSS_SELECTOR, "footer")

    close_security_alert_button = (By.CSS_SELECTOR, ".close")

    @staticmethod
    def go_to_search_result_page(browser):
        """ Метод перехода на страницу результатов поиска opencart  """

        browser.find_element(*CommonItems.search_button).click()

    @staticmethod
    def wait_element_present(wait, locator):
        """ Метод ожидания появления элемента """

        try:
            return wait.until(ec.presence_of_all_elements_located(locator))
        except Exception as exc:
            exc.msg = 'Unable to locate element by selector ' + str(locator)
            raise

    @staticmethod
    def close_security_alert(browser):
        """ Закрытие предупреждающего окна при загрузке страницы """

        browser.find_element(*CommonItems.close_security_alert_button).click()

    @staticmethod
    def accept_alert(browser):
        """ Нажимаем ОК на всплывающем окне """

        alert = browser.switch_to.alert
        alert.accept()

    @staticmethod
    def dismiss_alert(browser):
        """ Нажимаем ОК на всплывающем окне """

        alert = browser.switch_to.alert
        alert.dismiss()
