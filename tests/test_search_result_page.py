""" Тесты для страницы результата поиска"""

from pages.page_container import PageContainer
from pages.search_result_page import SearchResultPage


class TestSearchResultPage:
    """ Тесты для страницы результата поиска"""

    def test_search_result_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице результата поиска"""

        page = PageContainer(browser)

        browser.get(page.search_result.search_result_page_url)

        assert len(browser.find_elements(*page.search_result.search_input)) > 0

        assert len(browser.find_elements(*page.search_result.category_list)) > 0
        assert len(browser.find_elements(*page.search_result.category_desktops)) > 0
        assert len(browser.find_elements(*page.search_result.category_laptops_and_notebooks)) > 0
        assert len(browser.find_elements(*page.search_result.category_components)) > 0
        assert len(browser.find_elements(*page.search_result.category_tablets)) > 0
        assert len(browser.find_elements(*page.search_result.category_software)) > 0
        assert len(browser.find_elements(*page.search_result.category_phones_and_pdas)) > 0
        assert len(browser.find_elements(*page.search_result.category_cameras)) > 0
        assert len(browser.find_elements(*page.search_result.category_mp3_players)) > 0

        assert len(browser.find_elements(*page.search_result.subcategories_checkbox)) > 0
        assert len(browser.find_elements(
            *page.search_result.search_in_product_descriptions_checkbox)) > 0
        assert len(browser.find_elements(*page.search_result.search_button)) > 0
