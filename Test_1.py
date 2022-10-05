import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#Referencio el sitio web
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
# Usando selector xpath para obtener ruta del campo
nom=driver.find_element("xpath","//*[@id='userName']")
nom.send_keys("Jairo")
apellido=driver.find_element("id","userEmail").send_keys("jairob@gmail.com")
time.sleep(2)
#refernciando elementos usando By
email=driver.find_element(By.ID,"currentAddress").send_keys("Carrera 20# 158-40")
time.sleep(2)
email=driver.find_element(By.ID,"permanentAddress").send_keys("Carrera 20# 158-40")
SubmitButton=driver.find_element("id","submit").click()
time.sleep(2)
driver.close()

