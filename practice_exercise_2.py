import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

#Iniciar sesión.
WebDriverWait(driver,5).until(expected_conditions.presence_of_element_located((By.ID,'email')))
driver.find_element(By.ID, 'email').send_keys('some@gmail.com')
driver.find_element(By.ID, 'password').send_keys('passwd')
driver.find_element(By.CLASS_NAME, "auth-form__button").click()


#Guardar el título de la publicación más reciente (el texto del elemento). Nombra la variable title_before. La necesitas para compararla con el nuevo título más adelante.
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'places__list')))
title_before = driver.find_element(By.XPATH, '//li[@class="places__item card"]//h2[@class="card__title"]').text
#print(title_before) = pyramid of giza


#Hacer clic en el botón que agrega una nueva publicación. Utiliza la búsqueda por clase para encontrar este elemento.
driver.find_element(By.CLASS_NAME, 'profile__add-button').click()

#Importar el módulo random y generar un nombre para la nueva publicación: agrega 3 dígitos aleatorios a la palabra "Tokio". Guarda el nuevo nombre en una variable llamada new_title. Debería ser algo como "Tokio312".
new_title = f'Tokio{random.randint(100, 999)}'

#En la nueva ventana, ingresar el valor almacenado en new_title en el campo Nombre
driver.find_element(By.NAME, 'name').send_keys(new_title)
#driver.find_element(By.ID, 'place-name')

# Insertar https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg en el campo Enlace. Puedes hacerlo usando la búsqueda por el atributo name.
driver.find_element(By.NAME, 'link').send_keys("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg")

#Guardar los datos que ingresaste. Utiliza la búsqueda por XPath. Después del elemento raíz, busca el elemento form y su atributo name.
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/form/button[2]').click()

#Esperar a que aparezca el botón que elimina la publicación.
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
    (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/button[2]')))
#Utilizar assert para comprobar que la tarjeta muestra el nombre correcto almacenado en new_title.
title_after = driver.find_element(By.XPATH, '//li[@class="places__item card"]//h2[@class="card__title"]').text
assert title_after == new_title

print(title_before)
print(title_after)
print(new_title)

#Cuenta el total de tarjetas, cuenta cuantas hay por su clase.
cards_before_del = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
print(f'Cartas antes de eliminar: {cards_before_del}')


#Click en el botón de eliminar
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/button[2]').click()

#Despues de eliminar buscamos el primer elemento y verificamos que su nombre sea el que esta en title before adding.
## Wait for the title of the most recent card to become equal to title_before

WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(
    (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"), title_before))
after_del = driver.find_element(By.XPATH, '//li[@class="places__item card"]//h2[@class="card__title"]').text
assert after_del == title_before


# Check that there is one less card now
cards_after_del = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
print(f'Cartas despues de eliminar: {cards_after_del}')
assert cards_before_del - cards_after_del == 1
##assert cards_after_del < cards_before_del
