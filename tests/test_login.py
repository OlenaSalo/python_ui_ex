from selene import browser, have


def test_can_login_with_valid_credentials_page_obj(app):
    login_page = app.login_page()
    login_page.open()
    login_page.login_as("admin", "123456")

    main_page = app.main_page()
    main_page.brand_name().should(have.text('QAGuild'))