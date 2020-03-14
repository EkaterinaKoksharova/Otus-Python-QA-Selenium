""" Тесты магазина opencart """


class TestCommon:
    """ Тесты магазина opencart """

    def test_opencart_main_page_is_open(self, url, browser):
        """ Проверка открытия страницы сайта opencart """

        browser.get(url)
        homepage_url = browser.current_url
        assert "opencart" in homepage_url
