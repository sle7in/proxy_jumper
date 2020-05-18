
import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import config
url = sys.argv[-1]
if not url.endswith("/"):
    url = None
    quit()

service = Service(config.selenium_driver)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(url)
# elem = driver.find_element_by_class_name("polldaddy-placeholder")
radio1 = driver.find_element_by_id(config.answer_id)
radio1.click()
vote = driver.find_element_by_id(config.vote_button)
vote.click()
time.sleep(5) # quits web instance after voting
driver.quit()