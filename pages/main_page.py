""" Локаторы и методы главной страницы сайта opencart """

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    """ Локаторы и методы главной страницы сайта opencart """

    def __init__(self, logger, browser, common_items):
        super().__init__(logger, browser)
        self.common_items = common_items

    slider = (By.CSS_SELECTOR, ".swiper-viewport #slideshow0")
    slider_footer = (By.CSS_SELECTOR, ".swiper-viewport #carousel0")

    featured_card_1 = (By.CSS_SELECTOR, "#content .row > :nth-child(1)")
    featured_card_2 = (By.CSS_SELECTOR, "#content .row > :nth-child(2)")
    featured_card_3 = (By.CSS_SELECTOR, "#content .row > :nth-child(3)")
    featured_card_4 = (By.CSS_SELECTOR, "#content .row > :nth-child(4)")

    def go_to_main_page(self):
        """ Метод открытия главной страницы сайта opencart """

        with allure.step("Переход на страницу main"):
            self.logger.info('User is on the Main Page')
            self.browser.get(self.common_items.base_url)
