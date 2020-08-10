*** Settings ***
Documentation    Suite description

Library          Selenium2Library
Library          ../libraries/LoginLibrary.py


*** Test Cases ***
Авторизация в админской части opencart:

    Авторизоваться в opencart admin
    Дождаться присутствия кнопки admin logout

Авторизация в клиентской части opencart:

    Авторизоваться в opencart client
    Дождаться присутствия кнопки client logout
