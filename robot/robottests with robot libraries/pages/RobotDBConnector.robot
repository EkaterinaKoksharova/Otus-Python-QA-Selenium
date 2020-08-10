*** Settings ***
Documentation     Suite description
Library           Selenium2Library
Library           DatabaseLibrary


*** Keywords ***
Подключиться к базе
    Connect to database     dbapiModuleName=pymysql
    ...                     dbName=opencart
    ...                     dbUsername=ocadmin
    ...                     dbPassword=password
    ...                     dbHost=localhost
    ...                     dbPort=8889

Отключиться от базы
    Disconnect from database

Получить инфо из БД о добавленном продукте:
    [Arguments]     ${PRODUCT_NAME}
    Check if exists in database   SELECT * FROM oc_product_description WHERE name='${PRODUCT_NAME}'

Посчитать количество продуктов
    [Arguments]     ${rowCount}
    ${rowCount}     row count   SELECT * FROM oc_product

Проверить, что количество продуктов изменилось:
    [Arguments]     ${PRODUCT_COUNT_VARIABLE1}  ${PRODUCT_COUNT_VARIABLE2}
    Should not be equal   ${PRODUCT_COUNT_VARIABLE1}  ${PRODUCT_COUNT_VARIABLE2}
