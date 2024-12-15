
def test_register(pages):
    pages.homepage.click_register()
    pages.register_page.registration(gender='female',
                        first_name='Aswini',
                        last_name='s',
                        email='sas@gmail.com',
                        password='abc@1234',
                        confirm_pwd='abc@1234')







