import time
import random

import requests
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html

print('WU-73 Setup Bank Account (Generic Scenario)')
class TestSelenium(unittest.TestCase):

    def test_email_confirmation_flow(self):
        #first_email_xpath = '//*[@id="mr_132702533"]/td[2]'
        value = random.randint(999999999,99999999999999999)
        print ("Randon value:",value,) 

        signup_form_driver = webdriver.Chrome()
        signup_form_driver.maximize_window()
        signup_form_driver.get('https://app.dev.marketaccess.com/login')
        signup_form_driver.find_element_by_xpath('').send_keys('hubertbristow@gmail.com')
        signup_form_driver.find_element_by_xpath('').send_keys('TestPassword')
        signup_form_driver.find_element_by_css_selector('').click()
        time.sleep(5)

        signup_form_driver.find_element_by_xpath('').send_keys('hubertbristow@gmail.com')
        signup_form_driver.find_element_by_xpath('').send_keys('TestPassword')
        signup_form_driver.find_element_by_css_selector('').click()

        signup_form_driver.find_element_by_xpath('').send_keys('hubertbristow@gmail.com')
        signup_form_driver.find_element_by_xpath('').send_keys('TestPassword')
        signup_form_driver.find_element_by_css_selector('').click()
        time.sleep(3)

        signup_form_driver.find_element_by_xpath('').send_keys('hubertbristow@gmail.com')
        signup_form_driver.find_element_by_xpath('').send_keys('TestPassword')
        signup_form_driver.find_element_by_css_selector('').click()
        time.sleep(3)

        signup_form_driver.find_element_by_xpath('').send_keys('hubertbristow@gmail.com')
        signup_form_driver.find_element_by_xpath('').send_keys('TestPassword')
        signup_form_driver.find_element_by_css_selector('').click()
        time.sleep(3)
        
        signup_form_driver.find_element_by_xpath('').send_keys('hubertbristow@gmail.com')
        signup_form_driver.find_element_by_xpath('').send_keys('TestPassword')
        signup_form_driver.find_element_by_css_selector('').click()
        time.sleep(3)

if __name__=='__main__':
    unittest.main()

