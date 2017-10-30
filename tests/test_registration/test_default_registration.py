from pages.registration_page import RegistrationPage


def test_default_registration():

    page = RegistrationPage()

    page.get_registration_form()
    page.register_new_user()

    page.assert_text_is_displayed("We will send you an email shortly to verify your address.")
