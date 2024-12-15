import time
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver as chr_driver
from Scripts.Library.Generic_functions import Wrapper

driver = chr_driver()
driver.get('https://demowebshop.tricentis.com/computers')
wrapper = Wrapper(driver)

'task - 1 --> search'
# wrapper.refresh_page()
# wrapper.enter_text(('xpath', '//input[@class="search-box-text ui-autocomplete-input"]'), 'Computers')
# wrapper.maximize_browser()
# wrapper.click_element(('xpath', '//input[@class="button-1 search-box-button"]'))
# wrapper.minimize_browse()

'Task - 2 --> Register'
# wrapper.refresh_page()
# wrapper.maximize_browser()
# wrapper.click_element(('xpath', "//a[.='Register']"))
# wrapper.click_element(('xpath', '//input[@value="F"]'))
# wrapper.enter_text(('xpath', '//input[@id="FirstName"]'), "Aswini")
# wrapper.enter_text(('xpath', '//input[@id="LastName"]'), "S")
# wrapper.enter_text(('xpath', '//input[@id="Email"]'), "sashwini.2021@gmail.com")
# wrapper.enter_text(('xpath', '//input[@id="LastName"]'), "S")
# wrapper.enter_text(('xpath', '//input[@id="Password"]'), 'Achu@123')
# wrapper.enter_text(('xpath', '//input[@id="ConfirmPassword"]'), 'Achu@123')
# wrapper.click_element(('xpath', '//input[@id="register-button"]'))
# sleep(2)

'Task - 3 --> login'
# wrapper.refresh_page()
# wrapper.maximize_browser()
# wrapper.click_element(('xpath', "//a[.='Log in']"))
# wrapper.enter_text(('xpath', '//input[@id="Email"]'), 'sashwini.2021@gmail.com')
# wrapper.enter_text(('xpath', '//input[@id="Password"]'), 'Achu@123')
# wrapper.click_element(('xpath', '//input[@id="RememberMe"]'))
# wrapper.click_element(('xpath', '//input[@class="button-1 login-button"]'))
# sleep(2)

'Task - 4 --> scroll_up and scroll_down'
# wrapper.page_down_()
# wrapper.page_up_()
'Task - 5 --> arrow up and arrow down'
# for _ in range(5):
#     time.sleep(1)
#     wrapper.Arrow_down_()
# for _ in range(5):
#     time.sleep(1)
#     wrapper.Arrow_up_()

'Task - 6 --> context_click'
# wrapper.maximize_browser()
# wrapper.context_click(('xpath', '//ul[@class="top-menu"]/li/a[@href="/books"]'))
# time.sleep(2)

'Task - 7 --> double_click'
# wrapper.maximize_browser()
# wrapper.double_click(('xpath', "//a[.='Register']"))

'Task - 8 --> Drag_drop'
# driver.get('https://demoapps.qspiders.com/ui/dragDrop/dragToCorrect?sublist=2')
# wrapper.maximize_browser()
# source_ = ('xpath', "//div[.='Mobile Cover']")
# destination = ('xpath', '//div[@class="drop-column  min-h-[200px] bg-slate-100"]')
# wrapper.drag_drop(source_, destination)
# driver.quit()

'Task - 9 --> drop_down'
# driver.get('https://demoapps.qspiders.com/ui/dropdown?sublist=0')
# wrapper.maximize_browser()
# wrapper.drop_down(('xpath', '//select[@id="select3"]'), 'Canada')
# wrapper.drop_down(('xpath', '//select[@id="select1"]'), '+91')
# wrapper.drop_down(('xpath', '//select[@id="select2"]'), 'Female')
# wrapper.drop_down(('xpath', '//select[@id="select5"]'), 'Yukon')
# wrapper.drop_down(('xpath', "//select[.='Select City']"), 'Select City')
# time.sleep(3)







