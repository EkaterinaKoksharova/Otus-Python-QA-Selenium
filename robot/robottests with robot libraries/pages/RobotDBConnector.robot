*** Settings ***
Documentation     Suite description
Library           Selenium2Library
Library           DatabaseLibrary

Suite Setup       Connect to Database
...                dbapiModuleName=pymysql
...                dbName=opencart
...                dbUsername=ocadmin
...                dbPassword=password
...                dbHost=localhost
...                dbPort=8889


*** Keywords ***

Получить инфо из БД о добавленном продукте:
    [Arguments]     ${PRODUCT_NAME}
    Check if not exists in database   SELECT * FROM oc_product_description WHERE name=${PRODUCT_NAME}

Посчитать количество продуктов как:
    [Arguments]     ${PRODUCT_COUNT_VARIABLE}

    ${PRODUCT_COUNT_VARIABLE}    row count   SELECT * FROM oc_product

Проверить, что количество продуктов изменилось:
    [Arguments]     ${PRODUCT_COUNT_VARIABLE1}  ${PRODUCT_COUNT_VARIABLE2}
    Should not be equal as integers     ${PRODUCT_COUNT_VARIABLE1}  ${PRODUCT_COUNT_VARIABLE2}
