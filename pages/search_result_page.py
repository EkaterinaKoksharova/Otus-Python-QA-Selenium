""" Локаторы и методы страницы результата поиска сайта opencart """

from selenium.webdriver.common.by import By
from pages.common import CommonItems
from pages.base_page import BasePage


class SearchResultPage(BasePage):
    """ Локаторы и методы страницы результата поиска сайта opencart """

    def __init__(self, logger, browser, common_items):
        super().__init__(logger, browser)
        self.common_items = common_items

    search_result_page_url = CommonItems.base_url + "index.php?route=product/search"

    search_input = (By.CSS_SELECTOR, "#input-search")

    category_list = (By.CSS_SELECTOR, "[name='category_id']")
    category_desktops = (By.CSS_SELECTOR, "[name='category_id'] [value='20']")
    category_laptops_and_notebooks = (By.CSS_SELECTOR, "[name='category_id'] [value='18']")
    category_components = (By.CSS_SELECTOR, "[name='category_id'] [value='25']")
    category_tablets = (By.CSS_SELECTOR, "[name='category_id'] [value='57']")
    category_software = (By.CSS_SELECTOR, "[name='category_id'] [value='17']")
    category_phones_and_pdas = (By.CSS_SELECTOR, "[name='category_id'] [value='24']")
    category_cameras = (By.CSS_SELECTOR, "[name='category_id'] [value='33']")
    category_mp3_players = (By.CSS_SELECTOR, "[name='category_id'] [value='34']")

    subcategories_checkbox = (By.CSS_SELECTOR, "[name=sub_category]")

    search_in_product_descriptions_checkbox = (By.CSS_SELECTOR, "#description")
    search_button = (By.CSS_SELECTOR, "#content #button-search")

    view_result_as_list = (By.CSS_SELECTOR, "#list-view")
    view_result_as_grid = (By.CSS_SELECTOR, "#grid-view")
    product_compare_link = (By.CSS_SELECTOR, "#compare-total")
    sort_list = (By.CSS_SELECTOR, "#input-sort")
    set_items_quantity = (By.CSS_SELECTOR, "#input-limit")
    product_card = (By.CSS_SELECTOR, ".product-grid")

    def go_to_search_result_page(self):
        """ Метод перехода на страницу результатов поиска opencart """

        self.logger.info('User is on the Search Result page')
        self.browser.find_element(*self.common_items.search_button).click()
