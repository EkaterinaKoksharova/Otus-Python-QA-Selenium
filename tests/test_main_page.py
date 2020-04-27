""" Тесты для главной страницы магазина opencart """


from pages.page_container import PageContainer


class TestMainPage:
    """ Тесты для главной страницы магазина opencart """

    def test_main_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на главной странице"""

        page = PageContainer(browser)

        browser.get(page.common.base_url)
        assert len(browser.find_elements(*page.main.slider)) == 1
        assert len(browser.find_elements(*page.main.slider_footer)) == 1
        assert len(browser.find_elements(*page.main.featured_card_1)) == 1
        assert len(browser.find_elements(*page.main.featured_card_2)) == 1
        assert len(browser.find_elements(*page.main.featured_card_3)) == 1
        assert len(browser.find_elements(*page.main.featured_card_4)) == 1

    def test_go_to_search_result(self, browser):
        """ Проверка перехода на страницу результата поиска """

        page = PageContainer(browser)

        browser.get(page.common.base_url)
        page.common.go_to_search_result_page()

        assert browser.find_element(*page.search_result.search_input).is_displayed()
