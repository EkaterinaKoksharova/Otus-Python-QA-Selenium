""" Тесты для страницы администратора магазина opencart """

from Pages.admin_page import AdminPage


class TestAdminPage:
    """ Тесты для страницы администратора магазина opencart """

    def test_admin_login_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице логина администратора"""

        browser.get(AdminPage.adm_login_url)

        browser.find_element_by_css_selector(AdminPage.name_input)
        browser.find_element_by_css_selector(AdminPage.password_input)
        browser.find_element_by_css_selector(AdminPage.submit_button)
        browser.find_element_by_css_selector(AdminPage.forgotten_password_link)
        browser.find_element_by_css_selector(AdminPage.login_panel)
