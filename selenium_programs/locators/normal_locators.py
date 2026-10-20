from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()  #maximize the browser window

# id & name locators
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")


# linktext & partial linktext
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

#driver.close()
#driver.quit()

# ===============================================================================================================

# Class name tag name


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()  #maximize the browser window

sliders=driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(sliders)) #5    total number of sliders on home page

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links)) #  149 total number of links on home page


# ===============================================================================================================

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag & id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

# tag and class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

# tag & attribute
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc@gmail.com")


# tag , class & attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("xyz")




