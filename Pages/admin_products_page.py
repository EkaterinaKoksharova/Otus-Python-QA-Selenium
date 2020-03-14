""" Локаторы и методы страницы Products администратора магазина opencart"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.admin_page import AdminPage


class AdminProductsPage:
    """ Локаторы и методы страницы Products администратора магазина opencart """

    copy_button = (By.CSS_SELECTOR, ".fa-copy")
    add_button = (By.CSS_SELECTOR, ".fa-plus")
    product_form = (By.CSS_SELECTOR, "#form-product")
    delete_button = (By.CSS_SELECTOR, ".fa-trash-o")

    filter_button = (By.CSS_SELECTOR, "#button-filter")
    filter_name_input = (By.CSS_SELECTOR, "#input-name")
    filter_model_input = (By.CSS_SELECTOR, "#input-model")
    filter_price_button = (By.CSS_SELECTOR, "#input-price")
    filter_quantity_input = (By.CSS_SELECTOR, "#input-quantity")
    filter_status_input = (By.CSS_SELECTOR, "#input-status")
    filter_status_enabled = (By.CSS_SELECTOR, "#input-status [value='1']")
    filter_status_disabled = (By.CSS_SELECTOR, "#input-status [value='0']")

    select_all_products_checkbox = (By.CSS_SELECTOR, ".table thead [type='checkbox']")
    sort_by_name = (By.CSS_SELECTOR, "thead tr :nth-child(3)")
    sort_by_model = (By.CSS_SELECTOR, "thead tr :nth-child(4)")
    sort_by_price = (By.CSS_SELECTOR, "thead tr :nth-child(5)")
    sort_by_quantity = (By.CSS_SELECTOR, "thead tr :nth-child(6)")
    sort_by_status = (By.CSS_SELECTOR, "thead tr :nth-child(7)")

    product_lines = (By.CSS_SELECTOR, "tbody tr")
    product_line_name = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")
    select_product_checkbox = (By.CSS_SELECTOR, "tbody tr:nth-child(1) [type='checkbox']")
    edit_product_button = (By.CSS_SELECTOR, "tbody tr:nth-child(1) .btn")

    success_alert = (By.CSS_SELECTOR, ".alert-success")

    @staticmethod
    def go_to_products_page(browser, wait):
        """ Метод перехода на страницу products администраторской части opencart """

        browser.find_element(*AdminPage.menu_catalogue).click()

        wait.until(ec.visibility_of_element_located(AdminPage.menu_products))
        browser.find_element(*AdminPage.menu_products).click()
