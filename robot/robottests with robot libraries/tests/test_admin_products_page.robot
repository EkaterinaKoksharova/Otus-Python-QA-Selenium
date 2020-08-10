*** Settings ***
Documentation    Suite description
Library          Selenium2Library
Library           DatabaseLibrary

Resource        ../pages/RobotCommon.robot
Resource        ../pages/RobotAdminPage.robot
Resource        ../pages/RobotAdminProductsPage.robot
Resource        ../pages/RobotDBConnector.robot

Suite Setup     Подключиться к базе
Suite Teardown  Отключиться от базы
Test Teardown   Close browser

*** Variables ***
${PREVIOUS_PRODUCT_COUNT}
${ACTUAL_PRODUCT_COUNT}


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
    Получить инфо из БД о добавленном продукте:     ${TEST_PRODUCT_NAME}


Удаление продукта:

    Перейти на страницу авторизации admin
    Ввести логин и пароль
    Кликнуть на кнопку авторизации
    Закрыть предупреждающее окно
    Перейти на страницу products admin
    ${PREVIOUS_PRODUCT_COUNT}   row count   SELECT * FROM oc_product

    Удалить продукт                 ${TEST_PRODUCT_NAME}

    Подождать появления элемента:   ${ALERT_SUCCESS}
    ${ACTUAL_PRODUCT_COUNT}   row count   SELECT * FROM oc_product
    Проверить, что количество продуктов изменилось:     ${PREVIOUS_PRODUCT_COUNT}   ${ACTUAL_PRODUCT_COUNT}