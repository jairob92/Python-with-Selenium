import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
t=7
driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#Referencio el sitio web
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(7)
driver.get("https://www.google.com/")
time.sleep(7)
driver.get("https://www.vanguardia.com/")
driver.back()
time.sleep(7)
#otra forma de regresar a la pagina inicial en dado caso que el driver.back() no funcione
driver.execute_script("window.history.go(-1)")
time.sleep(7)
driver.close()
