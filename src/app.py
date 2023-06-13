from src.pages.episode_page import EpisodePage
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


class Application:

    def __init__(self, browser):
        self.browser = browser

    def auth(self):
        self.browser.driver.execute_script('window.localStorage.setItem(arguments[0], arguments[1]);',
                                           "access_token", "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjg2MzMxNzI5LCJleHAiOjE2ODY5MzY1Mjl9.NO5gghKyu00DQUYH4h1KnwLLVL4ama17AkeHbQOmSp_B7kr0qLNOPE16pKy4SvpScHY3x70DTdzpbhKlUGsUbQ")

    def login_page(self):
        return LoginPage(self.browser)

    def main_page(self):
        return MainPage(self.browser)

    def episode_page(self):
        return EpisodePage(self.browser)