import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import config

service = Service(config.chromedriver)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(config.site1)
# elem = driver.find_element_by_class_name("polldaddy-placeholder")
radio1 = driver.find_element_by_id("PDI_answer48849862")
radio1.click()
vote = driver.find_element_by_id("pd-vote-button10551560")
vote.click()
time.sleep(15) # quits web instance after voting
driver.quit()