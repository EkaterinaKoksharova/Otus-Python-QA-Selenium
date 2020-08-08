*** Settings ***
Documentation    Suite description
Library          Selenium2Library


*** Variables ***

${BROWSER}                  Chrome
${ALERT_SECURITY}           css:.close
${ALERT_ERROR}              css:.alert-danger
${ALERT_SUCCESS}            css:.alert-success


*** Keywords ***

Закрыть предупреждающее окно
    Click button    ${ALERT_SECURITY}

Подождать появления элемента:
    [Arguments]     ${element}
    Wait Until Element Is Visible      ${element}

Проверка, что в ссылке есть:
    [Arguments]     ${url_part}
    Location should contain      ${url_part}