from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from Scripts.POM.Homepage import HomePage
from Scripts.POM.Registerpage import RegisterPage
from Scripts.POM.Loginpage import LoginPage

'fixture'
'It is a design technique to provide datas to all the test methods'

@fixture()
def driver():
    driver_ = Chrome()
    driver_.get('https://demowebshop.tricentis.com/register')
    driver_.maximize_window()
    yield driver_
    driver_.close()

'Above process is called reset and trash process'

@fixture()
def pages(driver):
    class pages:
        homepage = HomePage(driver)
        register_page = RegisterPage(driver)
        login = LoginPage(driver)
    return pages()




