""" Тесты для страницы каталога магазина opencart """

from pages.catalogue_page import CataloguePage


class TestCataloguePage:
    """ Тесты для страницы каталога магазина opencart """

    def test_catalogue_page_find_elements(self, browser):
        """ Проверка наличия элементов на странице каталога"""

        browser.get(CataloguePage.catalogue_url)

        assert len(browser.find_elements(*CataloguePage.menu_left)) == 1

        assert len(browser.find_elements(*CataloguePage.view_result_as_list)) == 1
        assert len(browser.find_elements(*CataloguePage.view_result_as_grid)) == 1

        assert len(browser.find_elements(*CataloguePage.promo_banner)) == 1

        assert len(browser.find_elements(*CataloguePage.product_card_1)) == 1
        assert len(browser.find_elements(*CataloguePage.product_card_price)) == 1
        assert len(browser.find_elements(*CataloguePage.product_card_image)) == 1
        assert len(browser.find_elements(*CataloguePage.product_card_name_link)) == 1
        assert len(browser.find_elements(*CataloguePage.product_card_add_cart)) == 1
        assert len(browser.find_elements(*CataloguePage.product_card_add_wishlist)) == 1
        assert len(browser.find_elements(*CataloguePage.product_card_compare)) == 1
