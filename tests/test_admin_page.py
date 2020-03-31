""" Тесты для страницы администратора магазина opencart """

from pages.common import CommonItems
from pages.admin_page import AdminPage


class TestAdminPage:
    """ Тесты для страницы администратора магазина opencart """

    admin_wrong_pasword = "blabla"

    def test_admin_login_page_find_elements(self, browser, wait):
        """ Проверка наличия основных элементов на странице логина администратора"""

        AdminPage.go_to_admin_login_page(browser)

        assert len(CommonItems.wait_element_present(wait, AdminPage.name_input)) > 0
        assert len(CommonItems.wait_element_present(wait, AdminPage.submit_button)) > 0
        assert len(CommonItems.wait_element_present(wait, AdminPage.forgotten_password_link)) > 0
        assert len(CommonItems.wait_element_present(wait, AdminPage.login_panel)) > 0

    def test_login_to_admin_account_right(self, browser, wait):
        """ Проверка успешного входа в аккаунт администратора"""

        AdminPage.go_to_admin_login_page(browser)
        AdminPage.login_to_admin(browser)

        assert len(CommonItems.wait_element_present(wait, AdminPage.logout_button)) > 0

    def test_login_to_admin_account_wrong(self, browser, wait):
        """ Проверка НЕуспешного входа в аккаунт администратора (неверный пароль)"""

        AdminPage.go_to_admin_login_page(browser)
        AdminPage.login_to_admin(browser, AdminPage.admin_login, self.admin_wrong_pasword)

        assert len(CommonItems.wait_element_present(wait, AdminPage.alert_danger)) > 0

    def test_logout_from_admin_account(self, browser, wait):
        """ Проверка успешного выхода из аккаунта администратора"""

        AdminPage.go_to_admin_login_page(browser)
        AdminPage.login_to_admin(browser)
        CommonItems.wait_element_present(wait, AdminPage.logout_button)
        CommonItems.close_security_alert(browser)

        AdminPage.logout_from_admin(browser)

        assert len(CommonItems.wait_element_present(wait, AdminPage.login_panel)) > 0
