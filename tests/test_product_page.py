""" Тесты для страницы продукта магазина opencart """


from pages.page_container import PageContainer


class TestProductPage:
    """ Тесты для страницы продукта магазина opencart """

    def test_product_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице продукта"""

        page = PageContainer(browser)

        browser.get(page.product.product_page_url)

        assert len(browser.find_elements(*page.product.product_image)) == 1

        assert len(browser.find_elements(*page.product.description_tab)) == 1
        assert len(browser.find_elements(*page.product.description_content)) == 1

        assert len(browser.find_elements(*page.product.specification_tab)) == 1
        assert len(browser.find_elements(*page.product.specification_content)) == 1

        assert len(browser.find_elements(*page.product.reviews_tab)) == 1
        assert len(browser.find_elements(*page.product.reviews_content)) == 1

        assert len(browser.find_elements(*page.product.product_settings)) == 1
        assert len(browser.find_elements(*page.product.add_cart_button)) == 1
