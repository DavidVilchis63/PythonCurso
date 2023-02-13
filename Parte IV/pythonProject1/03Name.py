
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(3)

usuario = controlador.find_element(By.NAME, "email")
clave = controlador.find_element(By.NAME, "password")

usuario.send_keys("vilchizone@gmail.com")
clave.send_keys("12345678David")
time.sleep(2)

boton = controlador.find_element(By.CLASS_NAME, "helpers--auth-submit-button--2K2dh")
boton.click()
time.sleep(2)