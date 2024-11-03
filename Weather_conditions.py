import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_weather_for_selected_settlement():
    driver = webdriver.Chrome()
    # Abre la página principal
    driver.get('URL')

    # Espera a que se cargue la página
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located('localizador'))

    # Escribe la ubicación
    driver.find_element('localizador').send_keys('valor')
    # Selecciona la ubicación requerida de la lista sugerida
    driver.find_element('localizador').click()

    # Comprueba el nombre de la ubicación cuando se muestra la meteorología
    actually_settlement = driver.find_element('localizador').text
    expected_settlement = 'valor'
    assert expected_settlement == actually_settlement