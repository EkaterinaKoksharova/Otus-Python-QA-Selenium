""" Класс со свойством browser """


class BasePage:
    """ Класс со свойством browser """

    def __init__(self, logger, browser):
        self.logger = logger
        self.browser = browser
