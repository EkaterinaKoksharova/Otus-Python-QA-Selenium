""" Локаторы и методы главной страницы сайта opencart """

from selenium.webdriver.common.by import By


class MainPage:
    """ Локаторы и методы главной страницы сайта opencart """

    slider = (By.CSS_SELECTOR, ".swiper-viewport #slideshow0")
    slider_footer = (By.CSS_SELECTOR, ".swiper-viewport #carousel0")

    featured_card_1 = (By.CSS_SELECTOR, "#content .row > :nth-child(1)")
    featured_card_2 = (By.CSS_SELECTOR, "#content .row > :nth-child(2)")
    featured_card_3 = (By.CSS_SELECTOR, "#content .row > :nth-child(3)")
    featured_card_4 = (By.CSS_SELECTOR, "#content .row > :nth-child(4)")
