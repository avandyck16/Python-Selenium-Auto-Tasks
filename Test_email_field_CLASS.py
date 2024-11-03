import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPageAround:
    email = (By.ID, 'email')
    password = (By.ID, 'password')

    def __init__(self, driver):
     self.driver = driver

    def login_into_page(self):
        # Introduce el correo electrónico y la contraseña
        self.driver.find_element(*self.email).send_keys('correo@mail.com')
        self.driver.find_element(*self.password).send_keys('Contraseña')

    def check_mail_values(self):
        # Comprueba que el correo electrónico contiene los datos de entrada pasados
        actual_value = self.driver.find_element(*self.email).get_property("value")
        expected_value = 'correo@mail.com'
        assert actual_value == expected_value, f'Valor esperado de Correo electrónico: "{expected_value}", valor actual: "{actual_value}"'

    def check_pwd_values(self):
        # Comprueba que la contraseña contiene los datos de entrada pasados
        actual_value_pwd = self.driver.find_element(*self.password).get_property("value")
        expected_value_pwd = 'Contraseña'
        assert actual_value_pwd == expected_value_pwd, f'Valor esperado de Contraseña: "{expected_value_pwd}", valor actual: "{actual_value_pwd}"'


class TestLoginPage:
    #driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=en')
        cls.login_page = LoginPageAround(cls.driver)
        cls.wait = WebDriverWait(cls.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, 'email')))
        #Incluyo esta espera porque sin ella arroja un error, interactúa con el campo antes de que sea visible.

    def test_login_values(self):
        self.login_page.login_into_page()
        self.login_page.check_mail_values()
        self.login_page.check_pwd_values()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()