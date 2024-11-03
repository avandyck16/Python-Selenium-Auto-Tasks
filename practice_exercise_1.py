import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
driver.find_element(By.ID, "email").send_keys("some@mail.com")
driver.find_element(By.ID, "password").send_keys("passwd")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'card__image')))


# Hacer clic en la foto de perfil
driver.find_element(By.CLASS_NAME, 'profile__image').click()

# Insertar un enlace a la nueva foto
avatar_url = "https://ih1.redbubble.net/image.4711604228.4894/st,small,507x507-pad,600x600,f8f8f8.u3.jpg"
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.ID, 'owner-avatar')))
driver.find_element(By.ID, 'owner-avatar').send_keys(avatar_url)

# Guardar la nueva foto
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/form/button[2]').click()


# Esperando a que se cargue la foto de perfil
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'profile__image')))

# Save the value of the style attribute for the profile picture element to the style variable
WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".profile__image"), 'style', avatar_url))
style = driver.find_element(By.CSS_SELECTOR, '.profile__image').get_attribute('style')

# Check that style contains the link to the profile picture
assert avatar_url in style


driver.quit()