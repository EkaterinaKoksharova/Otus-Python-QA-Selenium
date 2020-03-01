""" Локаторы и методы страницы результата поиска сайта opencart """


class SearchResultPage:
    """ Локаторы и методы страницы результата поиска сайта opencart """

    search_result_page_url = "http://localhost:8080/opencart/index.php?route=product/search"

    search_input = "#input-search"

    category_list = "[name='category_id']"
    category_desktops = "[name='category_id'] [value='20']"
    category_laptops_and_notebooks = "[name='category_id'] [value='18']"
    category_components = "[name='category_id'] [value='25']"
    category_tablets = "[name='category_id'] [value='57']"
    category_software = "[name='category_id'] [value='17']"
    category_phones_and_pdas = "[name='category_id'] [value='24']"
    category_cameras = "[name='category_id'] [value='33']"
    category_mp3_players = "[name='category_id'] [value='34']"

    subcategories_checkbox = "[name=sub_category]"

    search_in_product_descriptions_checkbox = "#description"
    search_button = "#content #button-search"

    view_result_as_list = "#list-view"
    view_result_as_grid = "#grid-view"
    product_compare_link = "#compare-total"
    sort_list = "#input-sort"
    set_items_quantity = "#input-limit"
    product_card = ".product-grid"
