from Scripts.Library.Generic_functions import Wrapper

class HomePage(Wrapper):
    register_link = ('xpath', '//a[@class="ico-register"]')
    login_link = ('xpath', '//a[@class="ico-login"]')

    def __init__(self, driver):
        self.driver = driver


    def click_register(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.register_link)

    def click_login(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.login_link)



