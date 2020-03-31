""" Тесты для страницы результата поиска"""


from pages.search_result_page import SearchResultPage


class TestSearchResultPage:
    """ Тесты для страницы результата поиска"""

    def test_search_result_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице результата поиска"""

        browser.get(SearchResultPage.search_result_page_url)

        assert len(browser.find_elements(*SearchResultPage.search_input)) > 0

        assert len(browser.find_elements(*SearchResultPage.category_list)) > 0
        assert len(browser.find_elements(*SearchResultPage.category_desktops)) > 0
        assert len(browser.find_elements(*SearchResultPage.category_laptops_and_notebooks)) > 0
        assert len(browser.find_elements(*SearchResultPage.category_components)) > 0
        assert len(browser.find_elements(*SearchResultPage.category_tablets)) > 0
        assert len(browser.find_elements(*SearchResultPage.category_software)) > 0
        assert len(browser.find_elements(*SearchResultPage.category_phones_and_pdas)) > 0
        assert len(browser.find_elements(*SearchResultPage.category_cameras)) > 0
        assert len(browser.find_elements(*SearchResultPage.category_mp3_players)) > 0

        assert len(browser.find_elements(*SearchResultPage.subcategories_checkbox)) > 0
        assert len(browser.find_elements(
            *SearchResultPage.search_in_product_descriptions_checkbox)) > 0
        assert len(browser.find_elements(*SearchResultPage.search_button)) > 0
