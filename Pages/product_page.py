""" Локаторы и методы страницы товара сайта opencart """


class ProductPage:
    """ Локаторы и методы страницы товара сайта opencart """

    product_page_url = "http://localhost:8080/opencart/index.php?route=product/product&path=20&product_id=42"

    product_image = ".thumbnails :nth-child(1) a"
    product_image_close = ".mfp-close"
    product_image_slide_right = ".mfp-arrow-right"
    product_image_slide_left = ".mfp-arrow-left"

    description_tab = ".nav-tabs :nth-child(1) a"
    description_content = ".tab-content #tab-description"

    specification_tab = ".nav-tabs :nth-child(2) a"
    specification_content = ".tab-content #tab-specification"

    reviews_tab = ".nav-tabs :nth-child(3) a"
    reviews_content = ".tab-content #tab-review"

    product_settings = "#content #product"
    add_cart_button = "#product #button-cart"
