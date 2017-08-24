from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from time import sleep
import os
import datetime
import io
import random, string
import subprocess
import sys
from conf import *
import unittest


argument = sys.argv[1]

if argument == "1":
	driver = webdriver.Chrome('chromedriver.exe')
elif argument == "2":
	driver = webdriver.Ie('IEdriverserver.exe')

driver.maximize_window()

wait = WebDriverWait(driver, 15)

class TestWebUI(unittest.TestCase):
    def setUp(self):
        driver.get(baseURL)

    def test_that_it_loads(self):
        wait.until(EC.visibility_of_element_located((By.XPATH, regBtn)))
        assert (driver.find_element_by_xpath(regBtn).is_displayed()) is True

    def test_that_register_page_loads(self):
        driver.find_element_by_xpath(regBtn).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, cancelBtn)))
        assert (driver.find_element_by_xpath(cancelBtn).is_displayed()) is True


suite = unittest.TestLoader().loadTestsFromTestCase(TestWebUI)
unittest.TextTestRunner(verbosity=2).run(suite)

driver.quit()
