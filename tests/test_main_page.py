""" Тесты для главной страницы магазина opencart """


from pages.main_page import MainPage
from pages.common import CommonItems
from pages.search_result_page import SearchResultPage


class TestMainPage:
    """ Тесты для главной страницы магазина opencart """

    def test_main_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на главной странице"""

        browser.get(CommonItems.base_url)
        assert len(browser.find_elements(*MainPage.slider)) == 1
        assert len(browser.find_elements(*MainPage.slider_footer)) == 1
        assert len(browser.find_elements(*MainPage.featured_card_1)) == 1
        assert len(browser.find_elements(*MainPage.featured_card_2)) == 1
        assert len(browser.find_elements(*MainPage.featured_card_3)) == 1
        assert len(browser.find_elements(*MainPage.featured_card_4)) == 1

    def test_go_to_search_result(self, browser):
        """ Проверка перехода на страницу результата поиска """

        browser.get(CommonItems.base_url)
        CommonItems.go_to_search_result_page(browser)

        assert browser.find_element(*SearchResultPage.search_input).is_displayed()
