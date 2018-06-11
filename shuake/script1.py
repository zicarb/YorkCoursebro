#Thunder tech

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import unittest


class CourseSelect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/zombie/PycharmProjects/shuake/chromedriver')
        self.driver.get("https://wrem.sis.yorku.ca/Apps/WebObjects/REM")

    def testLogin(self):
        driver = self.driver
        PassportUsername = "zhx1997"
        PassportPassword = "zyx2018"
        term = int(1)
        wait = WebDriverWait(driver,20)

        accountNameId    = "mli"
        passFieldId      = "password"
        loginButtonXpath = "/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input"

        AccountNameIdElement = wait.until(lambda driver: driver.find_element_by_id(accountNameId))
        passFieldIdElement   = wait.until(lambda driver: driver.find_element_by_id(passFieldId))

        LoginButtonElement   = wait.until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        AccountNameIdElement.clear()
        AccountNameIdElement.send_keys(PassportUsername)
        time.sleep(3)
        passFieldIdElement.clear()
        passFieldIdElement.send_keys(PassportPassword)
        time.sleep(3)
        LoginButtonElement.click()
        driver=driver.current_window_handle
        driver
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
   unittest.main()


