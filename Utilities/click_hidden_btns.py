import time
from selenium.webdriver.common.by import By

class go_to_apt_page():
    def __init__(self, driver, URL):
        self.driver = driver
        self.URL = URL
    def loginPage(self):
        self.driver.get(self.URL)
    def click_hidden_btns(self):
        self.loginPage()
        time.sleep(1)
        expand_btn = self.driver.find_elements(By.XPATH,
                                  "//div[@class='css-1563yu1 r-djgu52 r-143r1dj r-n6v787'][contains(text(), '더 읽기')]")
        for i in expand_btn:
            i.click()