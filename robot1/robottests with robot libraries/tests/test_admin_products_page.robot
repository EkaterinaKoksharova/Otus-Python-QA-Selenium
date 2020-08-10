*** Settings ***
Documentation    Suite description
Library          Selenium2Library

Resource        ../pages/RobotCommon.robot
Resource        ../pages/RobotAdminPage.robot
Resource        ../pages/RobotAdminProductsPage.robot

Test Teardown   Close browser


*** Test Cases ***

Добавление нового продукта (НЕуспешное):
    # Заполняем не все обязательные поля (тег и модель не запонены)

    Перейти на страницу авторизации admin
    Ввести логин и пароль
    Кликнуть на кнопку авторизации
    Закрыть предупреждающее окно
    Перейти на страницу products admin
    Открыть форму добавления продукта
    Ввести наименование продукта:    ${TEST_PRODUCT_MODEL}
    Сохранить изменения продукта

    Подождать появления элемента:   ${ALERT_ERROR}

Добавление нового продукта (Успешное):

    Перейти на страницу авторизации admin
    Ввести логин и пароль
    Кликнуть на кнопку авторизации
    Закрыть предупреждающее окно
    Перейти на страницу products admin
    Добавить новый продукт          ${TEST_PRODUCT_NAME}    ${TEST_PRODUCT_TAG}     ${TEST_PRODUCT_MODEL}

    Подождать появления элемента:   ${ALERT_SUCCESS}

Удаление продукта:

    Перейти на страницу авторизации admin
    Ввести логин и пароль
    Кликнуть на кнопку авторизации
    Закрыть предупреждающее окно
    Перейти на страницу products admin
    Удалить продукт                 ${TEST_PRODUCT_NAME}

    Подождать появления элемента:   ${ALERT_SUCCESS}
