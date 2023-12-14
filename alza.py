from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.alza.cz/iphone-15?dq=7927612"
driver = webdriver.Edge()
driver.get(url)
driver.implicitly_wait(1)

price = driver.find_element(by=By.CLASS_NAME, value="price-box__price")
print(price.text)