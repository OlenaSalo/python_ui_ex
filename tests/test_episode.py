from selene import have
from selene.core.condition import not_

from src.api.episode import api_create_episode


def test_can_edit_episode(auth_app, faker):
    name = faker.name()
    episode = auth_app.episode_page()
    api_create_episode(name)
    episode.open()
    episode.delete_episode(name).click()
    episode.confirm_delete().click()
    episode.find_episode().should(not_(have.text(name)))