""" Локаторы и методы страницы Products администратора магазина opencart"""

import os
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class AdminProductsPage(BasePage):
    """ Локаторы и методы страницы Products администратора магазина opencart """

    def __init__(self, logger, browser, admin_page, common_items):
        super().__init__(logger, browser)
        self.admin_page = admin_page
        self.common_items = common_items

    product_photo_file_name = os.path.join(os.path.dirname(__file__),
                                           '/Users/zsergey/PycharmProjects/Otus-Python-QA-Selenium/'
                                           'pages/data/test_product_photo.jpg')

    copy_button = (By.CSS_SELECTOR, ".fa-copy")
    add_button = (By.CSS_SELECTOR, ".fa-plus")
    delete_button = (By.CSS_SELECTOR, ".fa-trash-o")

    product_form = (By.CSS_SELECTOR, "#form-product")
    product_form_save = (By.CSS_SELECTOR, "[data-original-title='Save']")
    product_form_cancel = (By.CSS_SELECTOR, "[data-original-title='Cancel']")
    product_form_general = (By.ID, "tab-general")
    product_form_data = (By.LINK_TEXT, "Data")
    product_form_image = (By.LINK_TEXT, "Image")

    product_form_general_name = (By.ID, "input-name1")
    product_form_general_metatag = (By.ID, "input-meta-title1")
    product_form_data_model = (By.ID, "input-model")
    product_form_image_add_image = (By.CSS_SELECTOR, "#tab-image #thumb-image")
    product_form_image_select_image = (By.CSS_SELECTOR, ".popover .fa-pencil")
    product_form_image_upload_image = (By.CSS_SELECTOR, "button .fa-upload")
    product_form_image_refresh = (By.CSS_SELECTOR, "#button-refresh.btn")

    filter_button = (By.CSS_SELECTOR, "#button-filter")
    filter_name_input = (By.CSS_SELECTOR, "#input-name")
    filter_model_input = (By.CSS_SELECTOR, "#input.log-model")
    filter_price_button = (By.CSS_SELECTOR, "#input.log-price")
    filter_quantity_input = (By.CSS_SELECTOR, "#input.log-quantity")
    filter_status_input = (By.CSS_SELECTOR, "#input.log-status")
    filter_status_enabled = (By.CSS_SELECTOR, "#input.log-status [value='1']")
    filter_status_disabled = (By.CSS_SELECTOR, "#input.log-status [value='0']")

    select_all_products_checkbox = (By.CSS_SELECTOR, ".table thead [type='checkbox']")
    sort_by_name = (By.CSS_SELECTOR, "thead tr :nth-child(3)")
    sort_by_model = (By.CSS_SELECTOR, "thead tr :nth-child(4)")
    sort_by_price = (By.CSS_SELECTOR, "thead tr :nth-child(5)")
    sort_by_quantity = (By.CSS_SELECTOR, "thead tr :nth-child(6)")
    sort_by_status = (By.CSS_SELECTOR, "thead tr :nth-child(7)")

    product_lines = (By.CSS_SELECTOR, "tbody tr")
    product_line_name = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")
    select_product_checkbox = (By.CSS_SELECTOR, "tbody tr:nth-child(1) [type='checkbox']")
    edit_product_button = (By.CSS_SELECTOR, "tbody tr:nth-child(1) .btn")

    success_alert = (By.CLASS_NAME, "alert-success")
    false_alert = (By.CLASS_NAME, "alert-danger")
    error_text = (By.CLASS_NAME, 'text-danger')

    def go_to_products_page(self, wait):
        """ Метод перехода на страницу products администраторской части opencart """

        with allure.step("Переход на страницу admin products"):
            self.logger.info('User is on the Admin Products Page')
            self.browser.find_element(*self.admin_page.menu_catalogue).click()

            wait.until(ec.visibility_of_element_located(self.admin_page.menu_products))
            self.browser.find_element(*self.admin_page.menu_products).click()

    def copy_product(self):
        """ Метод копирования 1го продукта на странице products администраторской части opencart """

        with allure.step("Копирование 1го продукта из списка"):
            self.browser.find_element(*self.select_product_checkbox).click()
            self.browser.find_element(*self.copy_button).click()

    def delete_product(self):
        """ Метод удаления 1го продукта на странице products администраторской части opencart """

        with allure.step("Удаление 1го продукта из списка"):
            self.browser.find_element(*self.select_product_checkbox).click()
            self.browser.find_element(*self.delete_button).click()

    def open_product_form_for_add(self):
        """ Метод открытия формы добавления нового продукта
        на странице products администраторской части opencart """

        with allure.step("Открытие формы добавления нового продукта"):
            self.browser.find_element(*self.add_button).click()

    def open_product_form_for_edit(self):
        """ Метод открытия формы редактирования нового продукта
        на странице products администраторской части opencart """

        with allure.step("Открытие формы редактирования продукта"):
            self.browser.find_element(*self.edit_product_button).click()

    def save_product_form(self):
        """ Метод сохранения изменений в форме продукта
                на странице products администраторской части opencart """

        with allure.step("Сохранение изменений в форме продукта"):
            self.browser.find_element(*self.product_form_save).click()

    def filter_products_by_name(self, product_name):
        """ Метод фильтрации продуктов по наименованию
                на странице products администраторской части opencart """

        with allure.step("Фильтрация продуктов по наименованию"):
            self.browser.find_element(*self.filter_name_input).send_keys(product_name)
            self.browser.find_element(*self.filter_button).click()

    def clear_filter(self):
        """ Метод очистки фильтров
                        на странице products администраторской части opencart """

        with allure.step("Очистка фильтров"):
            self.browser.find_element(*self.filter_name_input).clear()
            self.browser.find_element(*self.filter_button).click()

    def create_new_product_with_photo_load(self, photo_name, product_name, meta_tag_name, model_name):
        """ Создание нового продукта с загрузкой фото"""

        with allure.step("Создание нового продукта"):
            self.open_product_form_for_add()
            self.browser.find_element(*self.product_form_general_name).send_keys(product_name)
            self.browser.find_element(*self.product_form_general_metatag).send_keys(meta_tag_name)
            self.browser.find_element(*self.product_form_data).click()
            self.browser.find_element(*self.product_form_data_model).send_keys(model_name)

            self.browser.find_element(*self.product_form_image).click()
            self.browser.find_element(*self.product_form_image_add_image).click()

            self.browser.find_element(*self.product_form_image_select_image).click()

            #Клик по кнопке загрузки
            self.browser.execute_script("$('#button-upload').click();")

            #Показ формы загрузки фото на странице, ввод наименования файла фото
            self.browser.execute_script("$('#form-upload').show();")
            self.browser.execute_script("$('#form-upload > input.log').show();")

            self.browser.find_element_by_css_selector("#form-upload > input.log").send_keys(photo_name)

            self.common_items.accept_alert()

            self.browser.find_element(*self.product_form_image_refresh).click()
            self.browser.find_element_by_css_selector("[title='test_product_p hoto.jpg']").click()

            self.save_product_form()

    def create_new_product_without_photo_load(self, product_name, meta_tag_name, model_name):
        """ Создание нового продукта БЕЗ загрузки фото """

        with allure.step("Создание нового продукта БЕЗ загрузки фото"):
            self.open_product_form_for_add()
            self.browser.find_element(*self.product_form_general_name).send_keys(product_name)
            self.browser.find_element(*self.product_form_general_metatag).send_keys(meta_tag_name)
            self.browser.find_element(*self.product_form_data).click()
            self.browser.find_element(*self.product_form_data_model).send_keys(model_name)

            self.browser.find_element(*self.product_form_image).click()
            self.browser.find_element(*self.product_form_image_add_image).click()

            self.browser.find_element(*self.product_form_image_select_image).click()

            self.browser.find_element_by_css_selector("[title='cart.png']").click()

            self.save_product_form()
