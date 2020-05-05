""" Тесты магазина opencart """

from pages.page_container import PageContainer


class TestCommon:
    """ Тесты магазина opencart """

    def test_opencart_main_page_is_open(self, url, browser):
        """ Проверка открытия страницы сайта opencart """

        page = PageContainer(browser)
        page.tests_logger.info('test_opencart_main_page_is_open')

        browser.get(url)
        homepage_url = browser.current_url
        assert "opencart" in homepage_url

        assert "ERROR" not in str(browser.get_log("browser"))
