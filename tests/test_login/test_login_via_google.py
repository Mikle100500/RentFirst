from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from core.config import GOOGLE_EMAIL, GOOGLE_PASSWORD
from pages.gmail_page import GmailPage


def test_login_via_google():

    page = GmailPage()

    page.get_registration_form()
    page.click_google_login()
    page.login_to_gmail(GOOGLE_EMAIL, GOOGLE_PASSWORD)

    s('#search-form-link').should(have.text("MY SEARCH"))
    s('#my-account-link').should(have.text("MY ACCOUNT"))
    s('#login-logout-container').should(have.text("LOG OUT"))
