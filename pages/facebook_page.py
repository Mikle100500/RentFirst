from selene.support.jquery_style_selectors import s

from pages.registration_page import RegistrationPage


class FacebookPage(RegistrationPage):
    def login_to_facebook(self, email, password):
        s('#email').set_value(email)
        s('#pass').set_value(password).press_enter()
