import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#Referencio el sitio web
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
nombre=driver.find_element("xpath","//*[@id='userName']")
nombre.send_keys("Jairo")
nombre.send_keys(Keys.TAB +"Jairo@gmail.com"+ Keys.TAB +"Calle 20") #esta sentencia de codigo permite al campo username hacer tab y luego en el campo ingresar la informacion de email. Finalmente se hace tab y se ingresa la direccion
time.sleep(2)
PermanentAddress=driver.find_element(By.ID,"permanentAddress").send_keys("Carrera 20# 158-40")
driver.execute_script("window.scrollTo(0,300)")
SubmitButton=driver.find_element("id","submit").click()
time.sleep(2)
driver.close()
