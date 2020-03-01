""" Локаторы и методы главной страницы сайта opencart """


class MainPage:
    """ Локаторы и методы главной страницы сайта opencart """

    main_page_url = "http://localhost:8080/opencart/"

    slider = ".swiper-viewport #slideshow0"
    slider_footer = ".swiper-viewport #carousel0"

    featured_card_1 = "#content .row > :nth-child(1)"
    featured_card_2 = "#content .row > :nth-child(2)"
    featured_card_3 = "#content .row > :nth-child(3)"
    featured_card_4 = "#content .row > :nth-child(4)"