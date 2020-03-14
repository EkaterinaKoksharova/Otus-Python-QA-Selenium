""" Тесты для страницы администратора магазина opencart """

from pages.admin.admin_page import AdminPage


class TestAdminPage:
    """ Тесты для страницы администратора магазина opencart """

    def test_admin_login_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице логина администратора"""

        browser.get(AdminPage.adm_login_url)

        browser.find_element(*AdminPage.name_input)
        browser.find_element(*AdminPage.password_input)
        browser.find_element(*AdminPage.submit_button)
        browser.find_element(*AdminPage.forgotten_password_link)
        browser.find_element(*AdminPage.login_panel)
