""" Тесты для страницы продукта магазина opencart """


from pages.product_page import ProductPage


class TestProductPage:
    """ Тесты для страницы продукта магазина opencart """

    def test_product_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице продукта"""

        browser.get(ProductPage.product_page_url)

        browser.find_element(*ProductPage.product_image)

        browser.find_element(*ProductPage.description_tab)
        browser.find_element(*ProductPage.description_content)

        browser.find_element(*ProductPage.specification_tab)
        browser.find_element(*ProductPage.specification_content)

        browser.find_element(*ProductPage.reviews_tab)
        browser.find_element(*ProductPage.reviews_content)

        browser.find_element(*ProductPage.product_settings)
        browser.find_element(*ProductPage.add_cart_button)
