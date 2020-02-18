""" Тесты для главной страницы магазина opencart """


def test_opencart_min_page_is_open(url, browser):
    """ Проверка открытия страницы сайта opencart """

    browser.get(url)
    homepage_url = browser.current_url
    assert "opencart" in homepage_url
