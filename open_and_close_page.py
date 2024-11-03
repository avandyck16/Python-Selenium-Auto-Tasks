import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()

# Open the test stand page
driver.maximize_window()
driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')

# Check that /signin was added to the URL

assert '/signin' in driver.current_url

# Close the browser
driver.quit()

