""" Локаторы и методы страницы товара сайта opencart """

import allure
from selenium.webdriver.common.by import By
from pages.common import CommonItems
from pages.base_page import BasePage


class ProductPage(BasePage):
    """ Локаторы и методы страницы товара сайта opencart """

    def __init__(self, logger, browser):
        super().__init__(logger, browser)

    product_page_url = CommonItems.base_url + \
                       "index.php?route=product/product&path=20&product_id=40"

    product_image = (By.CSS_SELECTOR, ".thumbnails :nth-child(1) a")
    product_image_close = (By.CSS_SELECTOR, ".mfp-close")
    product_image_slide_right = (By.CSS_SELECTOR, ".mfp-arrow-right")
    product_image_slide_left = (By.CSS_SELECTOR, ".mfp-arrow-left")

    description_tab = (By.CSS_SELECTOR, ".nav-tabs :nth-child(1) a")
    description_content = (By.CSS_SELECTOR, ".tab-content #tab-description")

    specification_tab = (By.CSS_SELECTOR, ".nav-tabs :nth-child(2) a")
    specification_content = (By.CSS_SELECTOR, ".tab-content #tab-specification")

    reviews_tab = (By.CSS_SELECTOR, ".nav-tabs :nth-child(3) a")
    reviews_content = (By.CSS_SELECTOR, ".tab-content #tab-review")

    product_settings = (By.CSS_SELECTOR, "#content #product")
    add_cart_button = (By.CSS_SELECTOR, "#product #button-cart")

    def go_to_product_page(self):
        """ Метод открытия главной страницы сайта opencart """

        with allure.step("Переход на страницу product"):
            self.logger.info('User is on the Product Page')
            self.browser.get(self.product_page_url)
