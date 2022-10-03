from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
driver.close()

