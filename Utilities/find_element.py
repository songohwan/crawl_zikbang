from selenium import webdriver
from selenium.webdriver.common.by import By


class click_on_btns():
    def __init__(self, driver):
        self.driver = driver

    def getbytype(self, locatortype):
        if locatortype == 'XPATH':
            return By.XPATH

    def getelements(self, locatortype, XPATH_factor):
        byType = self.getByType(locatortype)
        element = self.driver.find_element(byType, XPATH_factor)
        return element