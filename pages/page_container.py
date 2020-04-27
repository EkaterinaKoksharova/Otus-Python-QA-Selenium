""" Класс с экземплярами классов всех страниц """

from Pages.admin_page import AdminPage
from Pages.admin_products_page import AdminProductsPage
from Pages.catalogue_page import CataloguePage
from Pages.common import CommonItems
from Pages.main_page import MainPage
from Pages.product_page import ProductPage
from Pages.search_result_page import SearchResultPage


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
