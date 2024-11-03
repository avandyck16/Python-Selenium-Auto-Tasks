from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")
time.sleep(5)
# Find all elements
elements = driver.find_elements(By.XPATH, '//img')

# Check that the number of elements found is greater than 1 by using len()
assert len(elements) > 1



# Close the browser
driver.quit()
