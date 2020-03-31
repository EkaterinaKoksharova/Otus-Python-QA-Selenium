""" Тесты для страницы Products администратора магазина opencart """

from pages.common import CommonItems
from pages.admin_page import AdminPage
from pages.admin_products_page import AdminProductsPage


class TestAdminProductsPage:
    """ Тесты для страницы Products администратора магазина opencart """

    product_name = 'Apple Cinema 30"'
    product_metatag = 'testtag'
    product_model = 'testmodel'

    def test_admin_products_page_find_elements(self, browser, wait):
        """ Проверка наличия основных элементов на странице логина администратора"""

        AdminPage.go_to_admin_login_page(browser)

        AdminPage.login_to_admin(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        assert len(CommonItems.wait_element_present(wait, AdminProductsPage.add_button)) > 0
        assert len(CommonItems.wait_element_present(wait, AdminProductsPage.copy_button)) > 0
        assert len(CommonItems.wait_element_present(wait, AdminProductsPage.delete_button)) > 0
        assert len(CommonItems.wait_element_present(wait, AdminProductsPage.filter_button)) > 0
        assert len(CommonItems.wait_element_present(
            wait, AdminProductsPage.select_all_products_checkbox)) > 0
        assert len(CommonItems.wait_element_present(wait, AdminProductsPage.product_lines)) > 0
        assert len(CommonItems.wait_element_present(
            wait, AdminProductsPage.select_product_checkbox)) > 0
        assert len(CommonItems.wait_element_present(
            wait, AdminProductsPage.edit_product_button)) > 0

    def test_copy_product(self, browser, wait):
        """ Проверка копирования продукта """

        AdminPage.go_to_admin_login_page(browser)

        AdminPage.login_to_admin(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        AdminProductsPage.copy_product(browser)

        CommonItems.wait_element_present(wait, AdminProductsPage.success_alert)
        CommonItems.wait_element_present(wait, AdminProductsPage.product_line_name)

        assert browser.find_element(
            *AdminProductsPage.product_line_name).text == self.product_name

    def test_delete_product_dismiss(self, browser, wait):
        """ Проверка отмены удаления продукта """

        AdminPage.go_to_admin_login_page(browser)

        AdminPage.login_to_admin(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        AdminProductsPage.delete_product(browser)
        CommonItems.dismiss_alert(browser)

        assert browser.find_element(
            *AdminProductsPage.product_line_name).text == self.product_name

    def test_delete_product(self, browser, wait):
        """ Проверка удаления продукта """

        AdminPage.go_to_admin_login_page(browser)

        AdminPage.login_to_admin(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        AdminProductsPage.delete_product(browser)
        CommonItems.accept_alert(browser)

        CommonItems.wait_element_present(wait, AdminProductsPage.success_alert)

        assert browser.find_element(
            *AdminProductsPage.product_line_name).text == self.product_name

    def test_open_add_new_product_form(self, browser, wait):
        """ Проверка открытия формы добавления нового продукта """

        AdminPage.go_to_admin_login_page(browser)

        AdminPage.login_to_admin(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        AdminProductsPage.open_product_form_for_add(browser)

        assert len(CommonItems.wait_element_present(wait, AdminProductsPage.product_form)) > 0

    def test_open_edit_product_form(self, browser, wait):
        """ Проверка открытия формы редактирования продукта """

        AdminPage.go_to_admin_login_page(browser)

        AdminPage.login_to_admin(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        AdminProductsPage.open_product_form_for_edit(browser)

        assert len(CommonItems.wait_element_present(wait, AdminProductsPage.product_form)) > 0

    def test_find_product_by_name(self, browser, wait):
        """ Проверка фильтрации списка продуктов по наименованию продукта """

        AdminPage.go_to_admin_login_page(browser)

        AdminPage.login_to_admin(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        all_products_quantity = len(browser.find_elements(*AdminProductsPage.product_lines))

        AdminProductsPage.filter_products_by_name(browser, self.product_name)

        filtered_products_quantity = \
            len(CommonItems.wait_element_present(wait, AdminProductsPage.product_lines))

        assert browser.find_elements(
            *AdminProductsPage.product_line_name)[0].text == self.product_name

        assert filtered_products_quantity != all_products_quantity

        AdminProductsPage.clear_filter(browser)

        assert len(browser.find_elements(*AdminProductsPage.product_lines)) == all_products_quantity

    def test_save_new_product_without_mandatory_fields(self, browser, wait):
        """ Проверка - нельзя сохранить новый продукт без имени, тега, модели """

        AdminPage.go_to_admin_login_page(browser)

        AdminPage.login_to_admin(browser)
        CommonItems.close_security_alert(browser)
        AdminProductsPage.go_to_products_page(browser, wait)

        AdminProductsPage.open_product_form_for_add(browser)
        AdminProductsPage.save_product_form(browser)

        assert len(browser.find_elements(*AdminProductsPage.error_text)) == 3
        assert len(CommonItems.wait_element_present(wait, AdminProductsPage.false_alert)) > 0
