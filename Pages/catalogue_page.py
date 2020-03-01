""" Локаторы и методы страницы каталога сайта opencart """


class CataloguePage:
    """ Локаторы и методы страницы каталога сайта opencart """

    catalogue_url = "http://localhost:8080/opencart/index.php?route=product/category&path=20"
    menu_left = ".list-group"

    view_result_as_list = "#list-view"
    view_result_as_grid = "#grid-view"

    promo_banner = ".swiper-wrapper"

    product_card_1 = "#content .row :nth-child(4) .product-thumb"
    product_card_price = "#content .row :nth-child(1) .product-thumb .price"
    product_card_image = "#content .row :nth-child(1) .product-thumb .image"
    product_card_name_link = "#content .row :nth-child(1) .product-thumb .caption a"
    product_card_add_cart = "#content .row :nth-child(1) .product-thumb .fa-shopping-cart"
    product_card_add_wishlist = "#content .row :nth-child(1) .product-thumb .fa-heart"
    product_card_compare = "#content .row :nth-child(1) .product-thumb .fa-exchange"

