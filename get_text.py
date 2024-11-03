import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Find the Email field and fill it in
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
##Estoy agregando esta espera porque el elemento tarda en cargar, y sin ella la prueba se detiene.
email = driver.find_element(By.ID, "email")
email.send_keys('mail@gmail.com')

# Find the Password field and fill it in
pwd = driver.find_element(By.ID, 'password')
pwd.send_keys('passwd')

# Find the Login button and click on it
login = driver.find_element(By.CLASS_NAME, 'auth-form__button')
login.click()

# Add an explicit wait for the page to load
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.header__logout')))

# Find the button, retrieve its text, and check that the text value is 'Logout'
logout = driver.find_element(By.CLASS_NAME, 'header__logout')
assert logout.text == 'Cerrar sesión'

driver.quit()
