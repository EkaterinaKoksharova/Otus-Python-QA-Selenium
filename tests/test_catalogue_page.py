""" Тесты для страницы каталога магазина opencart """

from pages.page_container import PageContainer


class TestCataloguePage:
    """ Тесты для страницы каталога магазина opencart """

    def test_catalogue_page_find_elements(self, browser):
        """ Проверка наличия элементов на странице каталога"""

        page = PageContainer(browser)

        browser.get(page.catalogue.catalogue_url)

        assert len(browser.find_elements(*page.catalogue.menu_left)) == 1

        assert len(browser.find_elements(*page.catalogue.view_result_as_list)) == 1
        assert len(browser.find_elements(*page.catalogue.view_result_as_grid)) == 1

        assert len(browser.find_elements(*page.catalogue.promo_banner)) == 1

        assert len(browser.find_elements(*page.catalogue.product_card_1)) == 1
        assert len(browser.find_elements(*page.catalogue.product_card_price)) == 1
        assert len(browser.find_elements(*page.catalogue.product_card_image)) == 1
        assert len(browser.find_elements(*page.catalogue.product_card_name_link)) == 1
        assert len(browser.find_elements(*page.catalogue.product_card_add_cart)) == 1
        assert len(browser.find_elements(*page.catalogue.product_card_add_wishlist)) == 1
        assert len(browser.find_elements(*page.catalogue.product_card_compare)) == 1
