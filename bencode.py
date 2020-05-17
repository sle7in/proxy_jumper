import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import config

service = Service(config.chromedriver)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
driver.quit()