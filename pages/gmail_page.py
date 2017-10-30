from selene.support import by
from selene.support.jquery_style_selectors import s

from pages.registration_page import RegistrationPage


class GmailPage(RegistrationPage):
    def login_to_gmail(self, email, password):
        s("#identifierId").set_value(email).press_enter()
        s(by.name("password")).send_keys(password).press_enter()
