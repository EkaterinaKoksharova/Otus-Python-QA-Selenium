*** Settings ***
Documentation  Suite description
Library     Selenium2Library

*** Variables ***

${BROWSER}  chrome
${LoginUrl}   https://localhost:8888/opencart/admin/
${AccountUrl}   https://www.ticketland.ru/private/
${login_input}=     name:LoginForm[contact]
${password_input}=      name:LoginForm[password]
${login_button}=    css:.registration-button
${logout_button}=   css:#tab_logout b

*** Keywords ***

Open ticketland login page
    Open browser    ${LoginUrl}      browser=${BROWSER}

Enter credentials
    [Arguments]     ${element}  ${login}
    Input text      ${element}  ${login}

Click login button
    Click button    ${login_button}

Wait logout button is visible
    Wait Until Element Is Visible   ${logout_button}

Assert curent url
    [Arguments]     ${Url}
    Location should be      ${Url}
