""" Класс с экземплярами классов всех страниц """

import logging
from pages.admin_page import AdminPage
from pages.admin_products_page import AdminProductsPage
from pages.catalogue_page import CataloguePage
from pages.common import CommonItems
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_result_page import SearchResultPage


class PageContainer:
    """ Класс с экземплярами классов всех страниц """

    def __init__(self, browser):
        self.logger = logging.getLogger("PAGE NAME")
        self.tests_logger = logging.getLogger("TEST NAME")
        self.common = CommonItems(self.logger, browser)
        self.admin = AdminPage(self.logger, browser)
        self.catalogue = CataloguePage(self.logger, browser, self.common)
        self.admin_products = AdminProductsPage(self.logger, browser, self.admin, self.common)
        self.main = MainPage(self.logger, browser, self.common)
        self.product = ProductPage(self.logger, browser)
        self.search_result = SearchResultPage(self.logger, browser, self.common)
