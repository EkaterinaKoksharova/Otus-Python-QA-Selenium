*** Settings ***
Documentation    Suite description
Library          Selenium2Library


*** Variables ***

${BROWSER}                  Chrome
${ALERT_DANGER}             css:.close


*** Keywords ***

Закрыть предупреждающее окно
    Click button    ${ALERT_DANGER}
    Wa

Подождать появления элемента
    [Arguments]     ${element}
    Wait Until Element Is Visible      ${element}