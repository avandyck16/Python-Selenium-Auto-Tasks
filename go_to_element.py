import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Find the Email field and fill it in
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
driver.find_element(By.ID, 'email').send_keys('some@gmail.com')

# Find the Password field and fill it in
driver.find_element(By.ID, 'password').send_keys('passwd')

# Find the Login button and click on it
driver.find_element(By.CLASS_NAME, 'auth-form__button').click()

# Add an explicit wait for the page to load
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'card__image')))

# Find the footer
footer = driver.find_element(By.TAG_NAME, 'footer')

# Scroll the footer into view
driver.execute_script("arguments[0].scrollIntoView();", footer)

# Check that the footer contains the string 'Around'
assert 'Around' in footer.text

driver.quit()


