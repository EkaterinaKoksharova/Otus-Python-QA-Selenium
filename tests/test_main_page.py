""" Тесты для главной страницы магазина opencart """

import allure
from pages.page_container import PageContainer


class TestMainPage:
    """ Тесты для главной страницы магазина opencart """

    page = PageContainer(browser=None)

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title("Проверка наличия основных элементов на главной странице")
    def test_main_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на главной странице """

        page = PageContainer(browser)
        page.tests_logger.info('test_main_page_find_elements')

        page.main.go_to_main_page()
        assert browser.find_element(*page.main.slider).is_displayed()
        assert browser.find_element(*page.main.slider_footer).is_displayed()
        assert browser.find_element(*page.main.featured_card_1).is_displayed()
        assert browser.find_element(*page.main.featured_card_2).is_displayed()
        assert browser.find_element(*page.main.featured_card_3).is_displayed()
        assert browser.find_element(*page.main.featured_card_4).is_displayed()

        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title("Проверка перехода на страницу результата поиска")
    def test_go_to_search_result(self, browser):
        """ Проверка перехода на страницу результата поиска """

        page = PageContainer(browser)
        page.tests_logger.info('test_go_to_search_result')

        browser.get(page.common.base_url)
        page.search_result.go_to_search_result_page()

        assert browser.find_element(*page.search_result.search_input).is_displayed()

        assert "ERROR" not in str(browser.get_log("browser"))
