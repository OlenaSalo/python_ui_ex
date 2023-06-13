import allure
from selene import have

from src.pages.page import Page


class LoginPage(Page):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Open login page")
    def open(self):
        self.browser.open("/login")

    @allure.step
    def login_as(self, user_name, user_password):
        self.browser.element("#usernameOrEmail").set_value(user_name)
        self.browser.element("#password").set_value(user_password)
        self.browser.element("//button[text()='Login']").click()
