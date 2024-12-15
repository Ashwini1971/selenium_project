from Scripts.Library.Generic_functions import Wrapper

class LoginPage:
    email_textfield = ('xpath', '//input[@name="Email"]')
    pwd_textfield = ('xpath', '//input[@name="Password"]')
    remember_me_checkbox = ('xpath', '//input[@type="checkbox"]')
    login_button = ('xpath', '//input[@class="button-1 login-button"]')

    def __init__(self, driver):
        self.driver = driver

    def login_(self, *, email, password):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.email_textfield, value=email)
        wrapper.enter_text(self.pwd_textfield, value=password)
        wrapper.click_element(self.remember_me_checkbox)
        wrapper.click_element(self.login_button)








