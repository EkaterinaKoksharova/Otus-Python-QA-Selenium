""" Тесты для страницы каталога магазина opencart """

from pages.catalogue_page import CataloguePage


class TestCataloguePage:
    """ Тесты для страницы каталога магазина opencart """

    def test_catalogue_page_find_elements(self, browser):
        """ Проверка наличия элементов на странице каталога"""

        browser.get(CataloguePage.catalogue_url)

        browser.find_element(*CataloguePage.menu_left)

        browser.find_element(*CataloguePage.view_result_as_list)
        browser.find_element(*CataloguePage.view_result_as_grid)

        browser.find_element(*CataloguePage.promo_banner)

        browser.find_element(*CataloguePage.product_card_1)
        browser.find_element(*CataloguePage.product_card_price)
        browser.find_element(*CataloguePage.product_card_image)
        browser.find_element(*CataloguePage.product_card_name_link)
        browser.find_element(*CataloguePage.product_card_add_cart)
        browser.find_element(*CataloguePage.product_card_add_wishlist)
        browser.find_element(*CataloguePage.product_card_compare)
