import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Log in
WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='email']")))
driver.find_element(By.ID, 'email').send_keys('some@gmail.com')
driver.find_element(By.ID, 'password').send_keys('passwd')
driver.find_element(By.CLASS_NAME, 'auth-form__button').click()

# Add an explicit wait for the feed to load
WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'places__list')))
WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'card__image')))
# Find the card and scroll it into view
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[7]/div[1]')
driver.execute_script("arguments[0].scrollIntoView();", element)

driver.quit()
