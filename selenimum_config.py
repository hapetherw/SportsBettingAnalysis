from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from config import SERVER_ENVIRONMENT

if SERVER_ENVIRONMENT:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = '/usr/bin/google-chrome'

    chrome_driver = '/usr/bin/chromedriver'
    browser = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
else:
    browser = webdriver.Chrome('chromedriver.exe')
