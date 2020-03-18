""" Тесты для страницы Products администратора магазина opencart """

from pages.common import CommonItems
from pages.admin_page import AdminPage
from pages.admin_products_page import AdminProductsPage


class TestAdminProductsPage:
    """ Тесты для страницы Products администратора магазина opencart """

    product_name = 'Apple Cinema 30"'

    def test_admin_products_page_find_elements(self, browser, wait):
        """ Проверка наличия основных элементов на странице логина администратора"""

        AdminPage.admin_login_right(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        browser.find_element(*AdminProductsPage.add_button)
        browser.find_element(*AdminProductsPage.copy_button)
        browser.find_element(*AdminProductsPage.delete_button)
        browser.find_element(*AdminProductsPage.filter_button)
        browser.find_element(*AdminProductsPage.select_all_products_checkbox)

        browser.find_element(*AdminProductsPage.product_lines)
        browser.find_element(*AdminProductsPage.select_product_checkbox)
        browser.find_element(*AdminProductsPage.edit_product_button)

    def test_copy_product(self, browser, wait):
        """ Проверка копирования продукта """

        AdminPage.admin_login_right(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        browser.find_element(*AdminProductsPage.select_product_checkbox).click()
        browser.find_element(*AdminProductsPage.copy_button).click()

        CommonItems.wait_element_present(wait, AdminProductsPage.success_alert)
        CommonItems.wait_element_present(wait, AdminProductsPage.product_line_name)

        assert browser.find_element(
            *AdminProductsPage.product_line_name).text == self.product_name

    def test_delete_product(self, browser, wait):
        """ Проверка удаления продукта """

        AdminPage.admin_login_right(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        browser.find_element(*AdminProductsPage.select_product_checkbox).click()
        browser.find_element(*AdminProductsPage.delete_button).click()
        CommonItems.accept_alert(browser)

        CommonItems.wait_element_present(wait, AdminProductsPage.success_alert)

        assert browser.find_element(
            *AdminProductsPage.product_line_name).text == self.product_name

    def test_open_add_new_product_form(self, browser, wait):
        """ Проверка открытия формы редактирования нового продукта """

        AdminPage.admin_login_right(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        browser.find_element(*AdminProductsPage.add_button).click()
        CommonItems.wait_element_present(wait, AdminProductsPage.product_form)

    def test_open_edit_product_form(self, browser, wait):
        """ Проверка открытия формы редактирования продукта """

        AdminPage.admin_login_right(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        browser.find_element(*AdminProductsPage.edit_product_button).click()
        CommonItems.wait_element_present(wait, AdminProductsPage.product_form)

    def test_find_product_by_name(self, browser, wait):
        """ Проверка фильтрации списка продуктов по наименованию продукта """

        AdminPage.admin_login_right(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        all_products_quantity = len(browser.find_elements(*AdminProductsPage.product_lines))

        browser.find_element(*AdminProductsPage.filter_name_input).send_keys(self.product_name)
        browser.find_element(*AdminProductsPage.filter_button).click()

        filtered_products_quantity = \
            len(CommonItems.wait_element_present(wait, AdminProductsPage.product_lines))

        assert browser.find_elements(
            *AdminProductsPage.product_line_name)[0].text == self.product_name

        assert filtered_products_quantity != all_products_quantity

        browser.find_element(*AdminProductsPage.filter_name_input).clear()
        browser.find_element(*AdminProductsPage.filter_button).click()

        assert len(browser.find_elements(*AdminProductsPage.product_lines)) == all_products_quantity
