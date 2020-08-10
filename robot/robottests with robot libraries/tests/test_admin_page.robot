*** Settings ***
Documentation    Suite description
Library          Selenium2Library

Resource        ../pages/RobotCommon.robot
Resource        ../pages/RobotAdminPage.robot
Resource        ../pages/RobotAdminProductsPage.robot

Test Teardown   Close browser


*** Test Cases ***
Авторизация (успешная) / выход из учетной записи:

    Перейти на страницу авторизации admin
    Ввести логин и пароль
    Кликнуть на кнопку авторизации
    Закрыть предупреждающее окно

    Выйти из учетной записи admin

    Проверка, что в ссылке есть:    login


Авторизация (НЕуспешная):

    Перейти на страницу авторизации admin
    Ввести логин и пароль   wrong_login     wrong_password
    Кликнуть на кнопку авторизации

    Подождать появления элемента:    ${ALERT_ERROR}
