""" Тесты для страницы каталога магазина opencart """

from pages.page_container import PageContainer


class TestCataloguePage:
    """ Тесты для страницы каталога магазина opencart """

    def test_catalogue_page_find_elements(self, browser):
        """ Проверка наличия элементов на странице каталога"""

        page = PageContainer(browser)
        page.tests_logger.info('test_catalogue_page_find_elements')

        page.catalogue.go_to_catalogue_page()

        assert browser.find_element(*page.catalogue.menu_left).is_displayed()

        assert browser.find_element(*page.catalogue.view_result_as_list).is_displayed()
        assert browser.find_element(*page.catalogue.view_result_as_grid).is_displayed()

        assert browser.find_element(*page.catalogue.promo_banner).is_displayed()

        assert browser.find_element(*page.catalogue.product_card_1).is_displayed()
        assert browser.find_element(*page.catalogue.product_card_price).is_displayed()
        assert browser.find_element(*page.catalogue.product_card_image).is_displayed()
        assert browser.find_element(*page.catalogue.product_card_name_link).is_displayed()
        assert browser.find_element(*page.catalogue.product_card_add_cart).is_displayed()
        assert browser.find_element(*page.catalogue.product_card_add_wishlist).is_displayed()
        assert browser.find_element(*page.catalogue.product_card_compare).is_displayed()

        assert "ERROR" not in str (browser.get_log ("browser"))
