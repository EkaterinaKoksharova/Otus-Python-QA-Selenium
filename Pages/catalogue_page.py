""" Локаторы и методы страницы каталога сайта opencart """

from selenium.webdriver.common.by import By
from pages.common import CommonItems


class CataloguePage:
    """ Локаторы и методы страницы каталога сайта opencart """

    catalogue_url = CommonItems.base_url + "index.php?route=product/category&path=20"
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
