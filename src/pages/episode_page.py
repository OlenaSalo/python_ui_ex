from src.pages.page import Page
from selene.core.entity import Element


class EpisodePage(Page):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.open("/list")

    _EPISODE = "//span[text()=' %s ']"
    _DELETE_BUTTON = f"{_EPISODE}/..//i"
    _CONFIRM_BUTTON = "//button/span[text()='%s']"

    def find_episode(self) -> Element:
        return self.browser.element(self._EPISODE)

    def delete_episode(self, name):
        return self.browser.element(self._DELETE_BUTTON % name)

    def confirm_delete(self, option="Yes"):
        return self.browser.element(self._CONFIRM_BUTTON % option)
