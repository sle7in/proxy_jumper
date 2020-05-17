import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service('C:/Users/ben4m/Repos/proxy_jumper/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
driver.quit()