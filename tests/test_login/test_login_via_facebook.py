from core.config import FACEBOOK_USERNAME_EMAIL, FACEBOOK_USERNAME_PASSWORD
from pages.facebook_page import FacebookPage
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s


def test_login_via_facebook():

    page = FacebookPage()

    page.get_registration_form()
    page.click_facebook_login()
    page.login_to_facebook(FACEBOOK_USERNAME_EMAIL, FACEBOOK_USERNAME_PASSWORD)

    s('#search-form-link').should(have.text("MY SEARCH"))
    s('#my-account-link').should(have.text("MY ACCOUNT"))
    s('#login-logout-container').should(have.text("LOG OUT"))
