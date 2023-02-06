from selenium import webdriver
from selenium.webdriver.common.by import By

import time

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://www.udemy.com/join/login-popup/?next=https%3A%2F%2Fwww.udemy.com%2Flogout%2F&skip_suggest=1&persist_locale=&locale=es_ES")
time.sleep(1)
usuario = controlador.find_element(By.ID, "form-group--1")
clave = controlador.find_element(By.ID, "form-group--3")

usuario.send_keys("vilchizone@gmail.com")
clave.send_keys("12345678David")
time.sleep(2)


