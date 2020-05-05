""" Тесты для страницы администратора магазина opencart """

from pages.page_container import PageContainer


class TestAdminPage:
    """ Тесты для страницы администратора магазина opencart """

    admin_wrong_pasword = "blabla"

    def test_admin_login_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице логина администратора"""

        page = PageContainer(browser)
        page.tests_logger.info('test_admin_login_page_find_elements')
        page.admin.go_to_admin_login_page()

        assert browser.find_element(*page.admin.name_input).is_displayed()
        assert browser.find_element(*page.admin.submit_button).is_displayed()
        assert browser.find_element(*page.admin.forgotten_password_link).is_displayed()
        assert browser.find_element(*page.admin.login_panel).is_displayed()

        assert "ERROR" not in str(browser.get_log("browser"))

    def test_login_to_admin_account_right(self, browser):
        """ Проверка успешного входа в аккаунт администратора"""

        page = PageContainer(browser)
        page.tests_logger.info('test_login_to_admin_account_right')
        page.admin.go_to_admin_login_page()
        page.admin.login_to_admin()

        assert browser.find_element(*page.admin.logout_button).is_displayed()
        assert "ERROR" not in str(browser.get_log("browser"))

    def test_login_to_admin_account_wrong(self, browser, wait):
        """ Проверка НЕуспешного входа в аккаунт администратора (неверный пароль)"""

        page = PageContainer(browser)
        page.tests_logger.info('test_login_to_admin_account_wrong')
        page.admin.go_to_admin_login_page()
        page.admin.login_to_admin(page.admin.login, self.admin_wrong_pasword)

        assert len(page.common.wait_element_present(wait, page.admin.alert_danger)) > 0
        assert "ERROR" not in str(browser.get_log("browser"))

    def test_logout_from_admin_account(self, browser, wait):
        """ Проверка успешного выхода из аккаунта администратора"""

        page = PageContainer(browser)
        page.tests_logger.info('test_logout_from_admin_account')

        page.admin.go_to_admin_login_page()
        page.admin.login_to_admin()
        page.common.wait_element_present(wait, page.admin.logout_button)
        page.common.close_security_alert()

        page.admin.logout_from_admin()

        assert len(page.common.wait_element_present(wait, page.admin.login_panel)) > 0
        assert "ERROR" not in str(browser.get_log("browser"))
