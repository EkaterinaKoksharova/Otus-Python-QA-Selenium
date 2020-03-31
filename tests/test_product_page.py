""" Тесты для страницы продукта магазина opencart """


from pages.product_page import ProductPage


class TestProductPage:
    """ Тесты для страницы продукта магазина opencart """

    def test_product_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице продукта"""

        browser.get(ProductPage.product_page_url)

        assert len(browser.find_elements(*ProductPage.product_image)) == 1

        assert len(browser.find_elements(*ProductPage.description_tab)) == 1
        assert len(browser.find_elements(*ProductPage.description_content)) == 1

        assert len(browser.find_elements(*ProductPage.specification_tab)) == 1
        assert len(browser.find_elements(*ProductPage.specification_content)) == 1

        assert len(browser.find_elements(*ProductPage.reviews_tab)) == 1
        assert len(browser.find_elements(*ProductPage.reviews_content)) == 1

        assert len(browser.find_elements(*ProductPage.product_settings)) == 1
        assert len(browser.find_elements(*ProductPage.add_cart_button)) == 1
