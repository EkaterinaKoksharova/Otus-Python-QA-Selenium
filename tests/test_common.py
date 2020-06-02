""" Тесты магазина opencart """

import allure
from pages.page_container import PageContainer


class TestCommon:
    """ Тесты магазина opencart """

    page = PageContainer(browser=None)

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title("Проверка открытия страницы сайта opencart")
    def test_opencart_main_page_is_open(self, url, browser):
        """ Проверка открытия страницы сайта opencart """

        page = PageContainer(browser)
        page.tests_logger.info('test_opencart_main_page_is_open')

        browser.get(url)
        homepage_url = browser.current_url
        assert "opencart" in homepage_url

        assert "ERROR" not in str(browser.get_log("browser"))
