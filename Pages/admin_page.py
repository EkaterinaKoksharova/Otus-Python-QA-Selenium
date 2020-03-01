""" Локаторы и методы страницы логина администратора сайта opencart """

import pytest


class AdminPage:
    """ Локаторы и методы страницы логина администратора сайта opencart """

    adm_login_url = "http://localhost:8080/opencart/admin/"
    login_panel = ".panel-default"
    name_input = "#input-username"
    password_input = "#input-password"
    submit_button = ".btn-primary"
    forgotten_password_link = ".help-block"
    error_message = '.alert-dismissible'
