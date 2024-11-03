import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')
time.sleep(2)

# Find the button and click on it

login_button = driver.find_element(By.XPATH, '//button[@class="auth-form__button"]')

login_button.click()
time.sleep(4)
driver.quit()


