import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(3)
# Find elements
email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'password')


# Test the placeholder attribute for each element
assert email.get_attribute('placeholder') == "Correo electrónico", f'El place holder es {email.get_attribute('placeholder')}, Esperado: "Correo Electrónico".'
assert password.get_attribute('placeholder') == "Contraseña", f'El place holder es {password.get_attribute('placeholder')}, Esperado: "Contraseña".'


# Close the browser
driver.quit()

## ==================== FORMA AUTOMATIZADA ========================= ##

def test_find_elements():
    email = driver.find_element(By.ID, 'email')
    password = driver.find_element(By.ID, 'password')
# Test the placeholder attribute for each element
    assert email.get_attribute('placeholder') == "Correo electrónico", f'El place holder es {email.get_attribute('placeholder')}, Esperado: "Correo Electrónico".'
    assert password.get_attribute('placeholder') == "Contraseña", f'El place holder es {password.get_attribute('placeholder')}, Esperado: "Contraseña".'
# Close the browser
    driver.quit()