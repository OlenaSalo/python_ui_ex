import allure
from selene import have

from src.pages.page import Page


class MainPage(Page):

    def __init__(self, broswer):
        super().__init__(broswer)

    @allure.step("The name of brand")
    def brand_name(self):
        return self.browser.element("//a[@class='navbar-brand']")

    
