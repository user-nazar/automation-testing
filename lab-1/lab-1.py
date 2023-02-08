import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin, log

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/math.html")

x = int(driver.find_element(By.ID, "input_value").text)
func = log(abs(12*sin(x)))
driver.find_element(By.ID, "answer").send_keys(func)
time.sleep(1)
driver.find_element(By.ID, "robotCheckbox").click()
time.sleep(1)
driver.find_element(By.ID, "robotsRule").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").submit()
time.sleep(10)






