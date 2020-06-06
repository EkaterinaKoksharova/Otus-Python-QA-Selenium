""" Тесты для страницы Products администратора магазина opencart """

import allure
import pytest
from pages.page_container import PageContainer


class TestAdminProductsPage:
    """ Тесты для страницы Products администратора магазина opencart """

    page = PageContainer(browser=None)
    product_name = 'Apple Cinema 30"'
    product_name_test = 'Apple Cinema 30" TEST'
    product_metatag = 'testtag'
    product_model = 'testmodel'

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title("Проверка наличия основных элементов на странице логина администратора")
    def test_admin_products_page_find_elements(self, browser, wait):
        """ Проверка наличия основных элементов на странице логина администратора"""

        page = PageContainer(browser)
        page.tests_logger.info('test_admin_products_page_find_elements')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        assert browser.find_element(*page.admin_products.add_button).is_displayed()
        assert browser.find_element(*page.admin_products.copy_button).is_displayed()
        assert browser.find_element(*page.admin_products.delete_button).is_displayed()
        assert browser.find_element(*page.admin_products.filter_button).is_displayed()
        assert browser.find_element\
            (*page.admin_products.select_all_products_checkbox).is_displayed()
        assert browser.find_element(*page.admin_products.product_lines).is_displayed()
        assert browser.find_element(*page.admin_products.select_product_checkbox).is_displayed()
        assert browser.find_element(*page.admin_products.edit_product_button).is_displayed()

        assert "ERROR" not in str(browser.get_log("browser"))

    @pytest.mark.skip
    def test_add_new_product_with_photo_load(self, browser, wait):
        """ Проверка добавления продукта """

        page = PageContainer(browser)
        page.tests_logger.info('test_add_new_product')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.create_new_product_with_photo_load\
            (page.admin_products.product_photo_file_name,
             self.product_name,
             self.product_metatag,
             self.product_model)

        assert len(page.common.wait_element_present(wait, page.admin_products.success_alert)) == 1
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка копирования продукта ")
    def test_add_new_product_without_photo_load(self, browser, wait):
        """ Проверка добавления продукта БЕЗ загрузки фото"""

        page = PageContainer(browser)
        page.tests_logger.info('test_add_new_product')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.create_new_product_without_photo_load(self.product_name,
                                                                  self.product_metatag,
                                                                  self.product_model)

        assert len(page.common.wait_element_present(wait, page.admin_products.success_alert)) == 1
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка копирования продукта ")
    def test_copy_product(self, browser, wait):
        """ Проверка копирования продукта """

        page = PageContainer(browser)
        page.tests_logger.info('test_copy_product')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.copy_product()

        page.common.wait_element_present(wait, page.admin_products.success_alert)
        page.common.wait_element_present(wait, page.admin_products.product_line_name)

        assert browser.find_element(
            *page.admin_products.product_line_name).text == self.product_name
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка отмены удаления продукта ")
    def test_delete_product_dismiss(self, browser, wait):
        """ Проверка отмены удаления продукта """

        page = PageContainer(browser)
        page.tests_logger.info('test_delete_product_dismiss')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.delete_product()
        page.common.dismiss_alert()

        assert browser.find_element(
            *page.admin_products.product_line_name).text == self.product_name
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка удаления продукта ")
    def test_delete_product(self, browser, wait):
        """ Проверка удаления продукта """

        page = PageContainer(browser)
        page.tests_logger.info('test_delete_product')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.delete_product()
        page.common.accept_alert()

        page.common.wait_element_present(wait, page.admin_products.success_alert)

        assert browser.find_element(
            *page.admin_products.product_line_name).text == self.product_name
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка открытия формы добавления нового продукта ")
    def test_open_add_new_product_form(self, browser, wait):
        """ Проверка открытия формы добавления нового продукта """

        page = PageContainer(browser)
        page.tests_logger.info('test_open_add_new_product_form')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.open_product_form_for_add()

        assert len(page.common.wait_element_present(wait, page.admin_products.product_form)) > 0
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка открытия формы редактирования продукта ")
    def test_open_edit_product_form(self, browser, wait):
        """ Проверка открытия формы редактирования продукта """

        page = PageContainer(browser)
        page.tests_logger.info('test_open_edit_product_form')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.open_product_form_for_edit()

        assert len(page.common.wait_element_present(wait, page.admin_products.product_form)) > 0
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка редактирования наименования продукта ")
    def test_edit_product_name(self, browser, wait):
        """ Проверка редактирования наименования продукта """

        page = PageContainer(browser)
        page.tests_logger.info('test_edit_product_name')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.open_product_form_for_edit()
        page.admin_products.edit_product_name(self.product_name_test)
        page.admin_products.edit_product_name(self.product_name)

        assert len(page.common.wait_element_present(wait, page.admin_products.product_form)) > 0
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка фильтрации списка продуктов по наименованию продукта ")
    def test_find_product_by_name(self, browser, wait):
        """ Проверка фильтрации списка продуктов по наименованию продукта """

        page = PageContainer(browser)
        page.tests_logger.info('test_find_product_by_name')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        all_products_quantity = len(browser.find_elements(*page.admin_products.product_lines))

        page.admin_products.filter_products_by_name(self.product_name)

        filtered_products_quantity = \
            len(page.common.wait_element_present(wait, page.admin_products.product_lines))

        assert browser.find_elements(
            *page.admin_products.product_line_name)[0].text == self.product_name

        assert filtered_products_quantity != all_products_quantity

        page.admin_products.clear_filter()

        assert len(browser.find_elements(
            *page.admin_products.product_lines)) == all_products_quantity
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title(" Проверка - нельзя сохранить новый продукт без имени, тега, модели ")
    def test_save_new_product_without_mandatory_fields(self, browser, wait):
        """ Проверка - нельзя сохранить новый продукт без имени, тега, модели """

        page = PageContainer(browser)
        page.tests_logger.info('test_save_new_product_without_mandatory_fields')

        page.admin.go_to_admin_login_page()

        page.admin.login_to_admin()
        page.common.close_security_alert()
        page.admin_products.go_to_products_page(wait)

        page.admin_products.open_product_form_for_add()
        page.admin_products.save_product_form()

        assert len(browser.find_elements(*page.admin_products.error_text)) == 3
        assert len(page.common.wait_element_present(wait, page.admin_products.false_alert)) > 0
        assert "ERROR" not in str(browser.get_log("browser"))
