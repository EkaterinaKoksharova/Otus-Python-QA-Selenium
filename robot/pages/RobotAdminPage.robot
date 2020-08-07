*** Settings ***
Documentation    Suite description
Library          Selenium2Library
Resource         RobotCommon.robot


*** Variables ***
${ADMIN_LOGIN_URL}          http://localhost:8888/opencart/admin/
${LOGIN_INPUT}           id:input-username
${PASSWORD_INPUT}           id:input-password
${LOGIN}                     admin
${PASSWORD}                 admin
${ALERT_DANGER}             css:.close
${LOGIN_BUTTON}             css:button[type='submit']
${MENU_CATALOG}                  css:li[id='menu-catalog']
${MENU_PRODUCTS}                 xpath=*//a[text()='Products']
${LOGOUT_BUTTON}            css:.fa-sign-out
${ADD_NEW_BUTTON}           xpath=//*[@id="content"]/div[1]/div/div/a/i
${PRODUCT_NAME_FIELD}       xpath=//*[@id="input-name1"]
${META_TAG_TITLE_FIELD}     xpath=//*[@id="input-meta-title1"]
${NAVIGATION_DATA}          xpath=//*[@id="form-product"]/ul/li[2]/a
${MODEL_FIELD}              xpath=//*[@id="input-model"]
${SAVE_BUTTON}              xpath=//*[@id="content"]/div[1]/div/div/button
${NEW_PRODUCT}              iPhone 11 Pro Max 64 GB
${NEW_TAG}                  iOS 13
${NEW_MODEL}                A2215
${PRODUCT_TO_DELETE}        xpath=//*[@id="form-product"]/div/table/tbody/tr[1]/td[1]/input
${DELETE_BUTTON}            xpath=//*[@id="content"]/div[1]/div/div/button[3]


*** Keywords ***

Перейти на страницу авторизации admin
    Open browser    ${ADMIN_LOGIN_URL}      browser=${BROWSER}

Ввести логин и пароль
    [Arguments]     ${password}=${PASSWORD}  ${login}=${LOGIN}
    Input text      ${LOGIN_INPUT}  ${login}
    Input text      ${PASSWORD_INPUT}  ${password}

Кликнуть на кнопку авторизации
    Click button    ${LOGIN_BUTTON}

Выйти из учетной записи admin
    Click button    ${LOGOUT_BUTTON}

#Подождать появления кнопки
#    Wait Until Element Is Visible   ${logout_button}

Assert curent url
    [Arguments]     ${Url}
    Location should be      ${Url}