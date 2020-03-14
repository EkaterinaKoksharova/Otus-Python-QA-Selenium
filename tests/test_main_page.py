""" Тесты для главной страницы магазина opencart """


from pages.main_page import MainPage
from pages.common import CommonItems


class TestMainPage:
    """ Тесты для главной страницы магазина opencart """

    def test_main_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на главной странице"""

        browser.get(CommonItems.base_url)
        browser.find_element(*MainPage.slider)
        browser.find_element(*MainPage.slider_footer)
        browser.find_element(*MainPage.featured_card_1)
        browser.find_element(*MainPage.featured_card_2)
        browser.find_element(*MainPage.featured_card_3)
        browser.find_element(*MainPage.featured_card_4)

    def test_go_to_search_result(self, browser):
        """ Проверка перехода на страницу результата поиска """

        browser.get(CommonItems.base_url)
        CommonItems.go_to_search_result_page(browser)
