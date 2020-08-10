*** Settings ***
Documentation    Suite description

Library          Selenium2Library
Library          ../libraries/LoginAdminLibrary.py
Library          ../libraries/LoginClientLibrary.py


*** Test Cases ***
Авторизация в админской части opencart:

    Перейти на страницу авторизации admin
    Ввести логин и пароль admin
    Кликнуть на кнопку авторизации admin
    Закрыть предупреждающее окно

    Дождаться присутствия кнопки admin logout

Авторизация в клиентской части opencart:

    Перейти на страницу авторизации client
    Ввести логин и пароль client
    Кликнуть на кнопку авторизации client

    Дождаться присутствия кнопки client logout
