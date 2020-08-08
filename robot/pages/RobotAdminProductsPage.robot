*** Settings ***
Documentation    Suite description
Library          Selenium2Library

Resource    RobotCommon.robot
Resource    RobotAdminPage.robot


*** Variables ***
${TEST_PRODUCT_NAME}            iPhone 11 Pro Max 64 GB
${TEST_PRODUCT_TAG}             iOS 13
${TEST_PRODUCT_MODEL}           A2215

${ADD_BUTTON}                   css:.fa-plus
${DELETE_BUTTON}                css:[data-original-title='Delete']
${COPY_BUTTON}                  css:.fa-copy
${SAVE_BUTTON}                  css:[data-original-title='Save']

${PRODUCT_NAME_INPUT}           id:input-name1
${PRODUCT_META_TAG_INPUT}       id:input-meta-title1
${PRODUCT_DATA}                 link:Data
${PRODUCT_MODEL_INPUT}          id:input-model

${FILTER_PRODUCT_NAME_INPUT}    id:input-name
${FILTER_PRODUCTS_BUTTON}       id:button-filter

${1ST_PRODUCT_CHECKBOX}         css:tbody tr:nth-child(1) [type='checkbox']


#    product_lines = (By.CSS_SELECTOR, "tbody tr")
#    product_line_name = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")
#    select_product_checkbox = (By.CSS_SELECTOR, "tbody tr:nth-child(1) [type='checkbox']")
#    edit_product_button = (By.CSS_SELECTOR, "tbody tr:nth-child(1) .btn")
#
#    error_text = (By.CLASS_NAME, 'text-danger')


*** Keywords ***

Перейти на страницу products admin
    Wait Until Element Is Visible      ${MENU_CATALOG}
    Click element       ${MENU_CATALOG}
    Wait Until Element Is Visible      ${MENU_PRODUCTS}
    Click element       ${MENU_PRODUCTS}

Добавить новый продукт
    [Arguments]         ${product_name}     ${meta_tag}     ${model}
    Click Element       ${ADD_BUTTON}
    Input text          ${PRODUCT_NAME_INPUT}    ${product_name}
    Input text          ${PRODUCT_META_TAG_INPUT}    ${meta_tag}
    Click Element       ${PRODUCT_DATA}
    Input text          ${PRODUCT_MODEL_INPUT}    ${model}
    Click Button        ${SAVE_BUTTON}

Открыть форму добавления продукта
    Click Element       ${ADD_BUTTON}

Ввести наименование продукта:
    [Arguments]         ${product_name}
    Input text          ${PRODUCT_NAME_INPUT}    ${product_name}

Сохранить изменения продукта
    Click Button        ${SAVE_BUTTON}

Удалить продукт
    [Arguments]         ${product_name}
    Input text          ${FILTER_PRODUCT_NAME_INPUT}     ${product_name}
    Click element       ${FILTER_PRODUCTS_BUTTON}
    Click element       ${1ST_PRODUCT_CHECKBOX}
    Click element       ${DELETE_BUTTON}
    Handle alert
