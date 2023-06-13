import configparser
import os
import sys

import pytest
from faker import Faker
from selene import browser

from selene.support.shared import config
from selenium import webdriver

from src.app import Application

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="default", help="env variable name"
    )

def read_ini():
    config_file_name = os.environ.get("config-file", "project-config.ini")
    root_path = os.path.join(sys.path[0], config_file_name)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser


def get_config(request):
    env_name = request.config.getoption("--env")
    try:
         return env_name, read_ini()[env_name]
    except KeyError:
        raise Exception(f"Wrong configuration for env name [{env_name}] NOT present")


def get_driver(env):
    if env == "local":
        return "chrome"

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "",
        "moon:options": {
            "enableVideo": False
        }
    }
    return webdriver.Remote(
        command_executor="http://192.168.64.2:4444/wd/hub",
        desired_capabilities = capabilities)



@pytest.fixture(scope="session")
def driver(request):

    env_name, app_config = get_config(request)
    browser.config.driver = get_driver(env_name)
    # browser.config.driver = "chrome"
    browser.config.base_url = app_config['base_url']
    browser.config.timeout = 4
    browser.config.window_width = int(app_config['window_width'])
    browser.config.window_height = int(app_config['window_height'])
    yield browser
    browser.close_current_tab()


@pytest.fixture(scope="session")
def app(driver):
    return Application(driver)


@pytest.fixture(scope="session")
def auth_app(app):
    login_page = app.login_page()
    login_page.open()
    app.auth()
    return app


@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker()
