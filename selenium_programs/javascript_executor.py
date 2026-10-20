# Common JavaScript Executor programs

# Program 1: Open a website and change the page background color
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

driver.execute_script("document.body.style.backgroundColor = 'yellow'")
driver.quit()

# ===================================================================================================================


# Program 2: Enter text into a textbox using JavaScript

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
driver.execute_script("arguments[0].value = 'tomsmith';", username)
driver.quit()

# ===================================================================================================================

# Program 3: Click a button using JavaScript

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

button = driver.find_element(
    By.XPATH, "//button[text()='Click for JS Alert']"
)

driver.execute_script("arguments[0].click();", button)

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.quit()


# ===================================================================================================================

# Program 4: Scroll down the webpage

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.quit()

# ===================================================================================================================

# Program 5: Scroll until an element is visible
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

element = driver.find_element(By.LINK_TEXT, "Infinite Scroll")

driver.execute_script(
    "arguments[0].scrollIntoView(true);", element
)

driver.quit()




# ===================================================================================================================

# Program 6: Get the page title using JavaScript

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

title = driver.execute_script("return document.title")
print(title)
driver.quit()


# ===================================================================================================================

# Program 7: Highlight an element

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

element = driver.find_element(By.ID, "username")

driver.execute_script(
    "arguments[0].style.border = '3px solid red';", element
)

driver.quit()


