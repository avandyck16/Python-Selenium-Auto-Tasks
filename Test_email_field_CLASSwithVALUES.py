from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class LoginPageAround:
    email_field = (By.ID, 'email')
    password_field = (By.ID, 'password')

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def check_email_value(self, email):
        actual_value = self.driver.find_element(*self.email_field).get_property("value")
        expected_value = email
        assert actual_value == expected_value

    def check_password_value(self,password):
        actual_password = self.driver.find_element(*self.password_field).get_property("value")
        expected_password = password
        assert actual_password == expected_password

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
        self.login_page.set_email('correo@mail')
        self.login_page.set_password('Contraseña')
        self.login_page.check_email_value('correo@mail')
        self.login_page.check_password_value('Contraseña')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()