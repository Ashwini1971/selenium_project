from Scripts.Library.Generic_functions import Wrapper
from Scripts.POM.Homepage import HomePage

class RegisterPage(HomePage):
    female_button = ('xpath', '//input[@id="gender-female"]')
    male_button = ('xpath', '//input[@id="gender-male"]')
    first_name_txtfld = ('xpath', '//input[@name="FirstName"]')
    last_name_txtfld = ('xpath', '//input[@name="LastName"]')
    email_txtfld = ('xpath', '//input[@name="Email"]')
    password_txtfld = ('xpath', '//input[@name="Password"]')
    confirm_pwd_txtfld = ('xpath', '//input[@name="ConfirmPassword"]')
    submit_button = ('xpath', '//input[@name="register-button"]')

    def registration(self, *, gender, first_name, last_name, email, password, confirm_pwd):
        wrapper = Wrapper(self.driver)
        if gender == 'female':
            wrapper.click_element(self.female_button)
        elif gender == 'male':
            wrapper.click_element(self.male_button)

        wrapper.enter_text(self.first_name_txtfld, value=first_name)
        wrapper.enter_text(self.last_name_txtfld, value=last_name)
        wrapper.enter_text(self.email_txtfld, value=email)
        wrapper.enter_text(self.password_txtfld, value=password)
        wrapper.enter_text(self.confirm_pwd_txtfld, value=confirm_pwd)
        wrapper.click_element(self.submit_button)





