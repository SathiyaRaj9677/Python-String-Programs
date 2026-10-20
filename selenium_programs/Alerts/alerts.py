
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automatically download and configure ChromeDriver
serv_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# Open the JavaScript Prompt
driver.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Prompt']"
).click()

time.sleep(2)

# Switch to the alert window
alertwindow = driver.switch_to.alert

# Print the alert message
print(alertwindow.text)

# Enter text into the prompt
alertwindow.send_keys("welcome")

# Close the prompt using Cancel
alertwindow.dismiss()

time.sleep(2)
driver.quit()



# Accept the alert


# Automatically download and configure ChromeDriver
# serv_obj = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://mypage.rediff.com/login/dologin")
# driver.maximize_window()

# driver.find_element(By.XPATH,"//input[@value='Login']").click() #lOGIN BUTTON
# time.sleep(5)
# driver.switch_to.alert.accept()

# driver.close()


