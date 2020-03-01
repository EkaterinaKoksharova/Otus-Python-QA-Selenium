""" Тесты для главной страницы магазина opencart """


from Pages.main_page import MainPage


class TestMainPage:
    """ Тесты для главной страницы магазина opencart """

    def test_main_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на главной странице"""

        browser.get(MainPage.main_page_url)
        browser.find_element_by_css_selector(MainPage.slider)
        browser.find_element_by_css_selector(MainPage.slider_footer)
        browser.find_element_by_css_selector(MainPage.featured_card_1)
        browser.find_element_by_css_selector(MainPage.featured_card_2)
        browser.find_element_by_css_selector(MainPage.featured_card_3)
        browser.find_element_by_css_selector(MainPage.featured_card_4)
