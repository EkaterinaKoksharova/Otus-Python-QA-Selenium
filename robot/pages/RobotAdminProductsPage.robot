*** Settings ***
Documentation    Suite description
Library          Selenium2Library

Resource    RobotCommon.robot
Resource    RobotAdminPage.robot


*** Variables ***
${ADMIN_LOGIN_URL}          http://localhost:8888/opencart/admin/
${PRODUCTS}                 xpath=*//a[text()='Products']
${LOGOUT_BUTTUN}            xpath=//*[@id="header"]/div/ul/li[2]/a/span
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

Перейти на страницу products admin
    Wait Until Element Is Visible      ${MENU_CATALOG}
    Click button    ${MENU_CATALOG}
    Wait Until Element Is Visible      ${MENU_PRODUCTS}
    Click button    ${MENU_PRODUCTS}
