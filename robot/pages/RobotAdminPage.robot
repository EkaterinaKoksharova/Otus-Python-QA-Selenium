*** Settings ***
Documentation    Suite description
Library          Selenium2Library
Resource         RobotCommon.robot


*** Variables ***
${ADMIN_LOGIN_URL}          http://localhost:8888/opencart/admin/

${LOGIN}                    admin
${PASSWORD}                 admin

${LOGIN_INPUT}              id:input-username
${PASSWORD_INPUT}           id:input-password
${LOGIN_BUTTON}             css:button.btn
${LOGOUT_BUTTON}            css:.fa-sign-out

${MENU_CATALOG}             id:menu-catalog
${MENU_PRODUCTS}            css:#collapse1 > :nth-child(2)


*** Keywords ***

Перейти на страницу авторизации admin
    Open browser    ${ADMIN_LOGIN_URL}      browser=${BROWSER}

Ввести логин и пароль
    [Arguments]     ${login}=${LOGIN}       ${password}=${PASSWORD}
    Input text      ${LOGIN_INPUT}  ${login}
    Input text      ${PASSWORD_INPUT}  ${password}

Кликнуть на кнопку авторизации
    Click button    ${LOGIN_BUTTON}

Выйти из учетной записи admin
    Click element    ${LOGOUT_BUTTON}
