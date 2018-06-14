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
        PassportUsername = ""
        PassportPassword = ""
        wait = WebDriverWait(driver,10)
        catnumber = ""

        accountNameId    = "mli"
        passFieldId      = "password"
        loginButtonXpath = "/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input"

        AccountNameIdElement = wait.until(lambda driver: driver.find_element_by_id(accountNameId))
        passFieldIdElement   = wait.until(lambda driver: driver.find_element_by_id(passFieldId))

        LoginButtonElement   = wait.until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        AccountNameIdElement.clear()
        AccountNameIdElement.send_keys(PassportUsername)

        passFieldIdElement.clear()
        passFieldIdElement.send_keys(PassportPassword)

        LoginButtonElement.click()

        enrollPageXpath = "/html/body/form/div[1]/table/tbody/tr[2]/td[2]/span/b"
        wait.until(lambda driver: driver.find_element_by_xpath(enrollPageXpath))

        submitButtonXpath = "/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input"

        select = Select(driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/span/select'))
        select.select_by_visible_text('FALL/WINTER 2018-2019 UNDERGRADUATE STUDENTS')
        driver.find_element_by_xpath(submitButtonXpath).click()

        TransferCourseXpath = "/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[4]/tbody/tr[1]/td[3]/div/input"
        TransferCourseElement = driver.find_element_by_xpath(TransferCourseXpath)
        TransferCourseElement.click()

        courseCatXpath = "/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/input[1]"
        courseCatElment = wait.until(lambda driver: driver.find_element_by_xpath(courseCatXpath))
        TransferconfirmXpath = "/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/input[2]"
        confirmElement = wait.until(lambda driver: driver.find_element_by_xpath(TransferconfirmXpath))

        courseCatElment.clear()
        courseCatElment.send_keys(catnumber)
        confirmElement.click()

        yesButtonXpath="/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[6]/td[2]/input[1]"
        yesButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(yesButtonXpath))
        yesButtonElement.click()
        check1Xpath = '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/span/font/b'
        try:
            wait.until(lambda driver: driver.find_element_by_xpath(check1Xpath))
        except:
            driver.save_screenshot('xxxxx.png')

    def tearDown(self):
        pass
