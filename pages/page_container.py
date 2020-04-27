""" Класс с экземплярами классов всех страниц """

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
        self.common = CommonItems(browser)
        self.admin = AdminPage(browser)
        self.catalogue = CataloguePage(browser, self.common)
        self.admin_products = AdminProductsPage(browser, self.admin, self.common)
        self.main = MainPage(browser)
        self.product = ProductPage(browser)
        self.search_result = SearchResultPage(browser)
