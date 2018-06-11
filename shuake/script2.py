from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
    def test_Login(self):
        driver = self.driver
        facebookUsername="zicarb@outlook.com"
        facebookPassword="oneshit1997!!"
        emilFieldID  ="email"
        passFieldId  ="pass"
        loginButtonXpath  ="//input[@value='Log In']"
        fbLogoXpath ="(//a[contains(@href,'logo')])[1]"


        emailFieldElment =WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emilFieldID))
        passFieldElment = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldId))
        loginButtonElment = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElment.clear()
        emailFieldElment.send_keys(facebookUsername)
        passFieldElment.clear()
        passFieldElment.send_keys(facebookPassword)
        WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()