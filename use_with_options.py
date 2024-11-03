from selenium import webdriver
import selenium
import time

chrome_options = webdriver.ChromeOptions() # Crea un objeto para la configuración
chrome_options.add_argument('--headless') # Ejecuta el navegador desde la terminal sin una interfaz gráfica
chrome_options.add_argument('--window-size=640,480') # Ajusta el tamaño de la ventana a 640 x 480 pixeles


# Initialize the driver with options
driver = webdriver.Chrome(options=chrome_options) # Crea un controlador y pasa la configuración de los ajustes establecidos
## Example with one config: driver = webdriver.Chrome(options=chrome_options.add_argument('--window-size=640,480'))




# Add a wait
time.sleep(5)

# Close the browser
driver.quit()
