import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
driver.maximize_window()
time.sleep(4)

# Find the title
form = driver.find_element(By.CLASS_NAME, "auth-form__textfield")

# Close the browser
driver.quit()
