from faker import Faker
from selene.browser import open_url
from selene.support import by
from selene.support.conditions import have, be
from selene.support.jquery_style_selectors import s

from core.config import GOOGLE_PASSWORD


class RegistrationPage(object):

    def open_main_page(self):
        open_url('https://marech.fr/')

    def click_sign_up(self):
        s('#login-logout-container').should(have.exact_text("SIGN UP")).click()

    def get_registration_form(self):
        self.open_main_page()
        self.click_sign_up()

    def click_facebook_login(self):
        s('#register .btn-facebook').should(be.visible).click()

    def click_google_login(self):
        s('#register .btn-google').should(be.visible).click()

    def register_new_user(self):
        name = Faker().name()
        email = Faker().email()
        self.set_name(name)
        self.set_email(email)
        self.set_password(GOOGLE_PASSWORD)
        s(by.xpath("//button[contains(text(), 'Create')]")).click()

    def set_name(self, name):
        s(by.name('create_name')).set_value(name)
        return self

    def set_email(self, email):
        s(by.name('create_email')).set_value(email)
        return self

    def set_password(self, password):
        s(by.name('create_password')).set_value(password)
        s(by.name('create_password2')).set_value(password)
        return self

    def assert_text_is_displayed(self, text):
        s(by.text(text)).should(be.visible)
