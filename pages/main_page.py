from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage): 
    def test1(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "a + .link")

        
        login_link.click()
        time.sleep(5)    
       	login_link = self.browser.find_element(By.XPATH, '//img[@alt="Семён Якушев"]')
       	login_link.click()
       	time.sleep(5) 
    def test2(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "nav a:last-child.link")
        login_link.click()
        time.sleep(5)
        login_link = self.browser.find_element(By.CSS_SELECTOR, "input.input.field").send_keys('Виктор')
        time.sleep(5)
        