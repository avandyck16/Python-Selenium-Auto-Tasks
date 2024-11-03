from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

## Quieres checar que exista un elemento: buscalo, encuentralo, y extrae el texto. El texto debe coincidir con lo
#que establezcas como esperado.


def test_email_and_password_value():
    driver = webdriver.Chrome()
    driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=en')

    # Introduce el correo electrónico
    WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.ID,'email')))
    driver.find_element(By.ID, 'email').send_keys('correo@mail.com')
    driver.find_element(By.ID, 'password').send_keys('Contraseña')

    # Comprueba que el correo electrónico contiene los datos de entrada pasados
    actual_value = driver.find_element(By.ID, 'email').get_property("value")
    expected_value = 'correo@mail.com'
    assert actual_value == expected_value, f'Valor esperado de Correo electrónico: "{expected_value}", valor actual: "{actual_value}"'

    # Comprueba que la contraseña contiene los datos de entrada pasados
    actual_value_pwd = driver.find_element(By.ID, 'password').get_property("value")
    expected_value_pwd = 'Contraseña'
    assert actual_value_pwd == expected_value_pwd, f'Valor esperado de Contraseña: "{expected_value}", valor actual: "{actual_value}"'

