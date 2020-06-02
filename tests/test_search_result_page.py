""" Тесты для страницы результата поиска"""

import allure
from pages.page_container import PageContainer


class TestSearchResultPage:
    """ Тесты для страницы результата поиска"""

    page = PageContainer(browser=None)

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title("Проверка наличия основных элементов на странице результата поиска")
    def test_search_result_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице результата поиска"""

        page = PageContainer(browser)
        page.tests_logger.info('test_search_result_page_find_elements')

        page.main.go_to_main_page()
        page.search_result.go_to_search_result_page()

        assert browser.find_element(*page.search_result.search_input).is_displayed()

        assert browser.find_element(*page.search_result.category_list).is_displayed()
        assert browser.find_element(*page.search_result.category_desktops).is_displayed()
        assert browser.find_element\
            (*page.search_result.category_laptops_and_notebooks).is_displayed()
        assert browser.find_element(*page.search_result.category_components).is_displayed()
        assert browser.find_element(*page.search_result.category_tablets).is_displayed()
        assert browser.find_element(*page.search_result.category_software).is_displayed()
        assert browser.find_element(*page.search_result.category_phones_and_pdas).is_displayed()
        assert browser.find_element(*page.search_result.category_cameras).is_displayed()
        assert browser.find_element(*page.search_result.category_mp3_players).is_displayed()

        assert browser.find_element(*page.search_result.subcategories_checkbox).is_displayed()
        assert browser.find_element\
            (*page.search_result.search_in_product_descriptions_checkbox).is_displayed()
        assert browser.find_element(*page.search_result.search_button).is_displayed()

        assert "ERROR" not in str(browser.get_log("browser"))
