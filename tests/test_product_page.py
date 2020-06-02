""" Тесты для страницы продукта магазина opencart """

import allure
from pages.page_container import PageContainer


class TestProductPage:
    """ Тесты для страницы продукта магазина opencart """

    page = PageContainer(browser=None)

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title("Проверка наличия основных элементов на странице продукта")
    def test_product_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице продукта"""

        page = PageContainer(browser)
        page.tests_logger.info('test_product_page_find_elements')

        page.product.go_to_product_page()

        assert browser.find_element(*page.product.product_image).is_displayed()

        assert browser.find_element(*page.product.description_tab).is_displayed()
        assert browser.find_element(*page.product.description_content).is_displayed()

        assert browser.find_element(*page.product.specification_tab).is_displayed()

        assert browser.find_element(*page.product.product_settings).is_displayed()
        assert browser.find_element(*page.product.add_cart_button).is_displayed()

        assert "ERROR" not in str(browser.get_log("browser"))
