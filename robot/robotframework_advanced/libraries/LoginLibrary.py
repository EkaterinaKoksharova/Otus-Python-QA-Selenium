from robot.api.deco import library, keyword

from robot.robotframework_advanced.libraries.LoginAdminLibrary import LoginAdminLibrary
from robot.robotframework_advanced.libraries.LoginClientLibrary import LoginClientLibrary


@library("LoginLibrary")
class LoginLibrary:

    ROBOT_LIBRARY_SCOPE = 'CLOBAL'

    def __init__(self):
        self.admin_login = LoginAdminLibrary()
        self.client_login = LoginClientLibrary()

    @keyword("Авторизоваться в opencart admin")
    def login_to_admin(self):
        """ Метод авторизации в opencart admin """

        self.admin_login.go_to_admin_login_page()
        self.admin_login.enter_admin_login_and_password()
        self.admin_login.click_admin_login_button()
        self.admin_login.close_security_alert()

    @keyword("Дождаться присутствия кнопки admin logout")
    def wait_admin_logout_button_present(self):
        """ Метод ожидания появления кнопки admin logout """

        wait = WebDriverWait(self.admin_login.a_browser, 10)
        wait.until(ec.presence_of_all_elements_located(self.admin_login.admin_logout_button))

    @keyword("Авторизоваться в opencart client")
    def login_to_admin(self):
        """ Метод авторизации в opencart client """

        self.client_login.go_to_client_login_page()
        self.client_login.enter_client_login_and_password()
        self.client_login.click_client_login_button()

    @keyword("Дождаться присутствия кнопки client logout")
    def wait_admin_logout_button_present(self):
        """ Метод ожидания появления кнопки client logout """

        wait = WebDriverWait(self.admin_login.a_browser, 10)
        wait.until(ec.presence_of_all_elements_located(self.admin_login.client_logout_button))
