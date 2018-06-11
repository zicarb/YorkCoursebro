#Thunder tech

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import unittest


class CourseTestSelect(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/zombie/PycharmProjects/shuake/chromedriver')
        self.driver.get("https://registar.yorku.ca")

    def testGotopage(self):
        driver = self.driver
        PassportUsername = "zhx1997"
        PassportPassword ="zyx2018"
        term = int(1)
        time.sleep(5)

        EnrollinclassXpath = "//*[@id='courses']/ul/li[6]/a"
        EnrollinclasseElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(EnrollinclassXpath))
        EnrollinclasseElement.click()

        driver = driver.current_window_handle
        AccountNameId    = "mli"
        passFieldId      = "password"
        LoginButtonXpath = "//input[@value = 'Login']"

        AccountNameIdElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(AccountNameId))
        passFieldIdElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldId))
        LoginButtonElement   = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(LoginButtonXpath))

        AccountNameIdElement.clear()
        AccountNameIdElement.send_keys(PassportUsername)
        time.sleep(3)
        passFieldIdElement.clear()
        passFieldIdElement.send_keys(PassportPassword)
        time.sleep(3)
        LoginButtonElement.click()

        driver = driver.current_window_handle
        select = Select(driver.find_element_by_value())
        select.select_by_value(term)
        driver.find_element_by_id("submit").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
