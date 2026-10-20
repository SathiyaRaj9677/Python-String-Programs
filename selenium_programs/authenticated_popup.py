
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automatically download and configure ChromeDriver
serv_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv_obj)

#driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.maximize_window()