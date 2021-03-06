""" Локаторы и методы страницы каталога сайта opencart """

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CataloguePage(BasePage):
    """ Локаторы и методы страницы каталога сайта opencart """

    def __init__(self, logger, browser, common_items):
        super().__init__(logger, browser)
        self.common_items = common_items
        self.catalogue_url = self.common_items.base_url + "index.php?route=product/category&path=20"

    menu_left = (By.CSS_SELECTOR, ".list-group")

    view_result_as_list = (By.CSS_SELECTOR, "#list-view")
    view_result_as_grid = (By.CSS_SELECTOR, "#grid-view")

    promo_banner = (By.CSS_SELECTOR, ".swiper-wrapper")

    product_card_1 = (By.CSS_SELECTOR,
                      "#content .row :nth-child(4) .product-thumb")
    product_card_price = (By.CSS_SELECTOR,
                          "#content .row :nth-child(1) .product-thumb .price")
    product_card_image = (By.CSS_SELECTOR,
                          "#content .row :nth-child(1) .product-thumb .image")
    product_card_name_link = (By.CSS_SELECTOR,
                              "#content .row :nth-child(1) .product-thumb .caption a")
    product_card_add_cart = (By.CSS_SELECTOR,
                             "#content .row :nth-child(1) .product-thumb .fa-shopping-cart")
    product_card_add_wishlist = (By.CSS_SELECTOR,
                                 "#content .row :nth-child(1) .product-thumb .fa-heart")
    product_card_compare = (By.CSS_SELECTOR,
                            "#content .row :nth-child(1) .product-thumb .fa-exchange")
    product_card_compare1 = (By.CSS_SELECTOR,
                             "#content .row :nth-child(1) .product-thumb .fa-exchange1")

    def go_to_catalogue_page(self):
        """ Метод открытия главной страницы сайта opencart """

        with allure.step("Переход на страницу catalogue"):
            self.logger.info('User is on the Catalogue Page')
            self.browser.get(self.catalogue_url)
