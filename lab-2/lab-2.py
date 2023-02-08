import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from math import sin, log


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

wait = WebDriverWait(driver, 120)
wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
driver.find_element(By.ID, 'book').click()

x = int(driver.find_element(By.ID, "input_value").text)
func = log(abs(12*sin(x)))
driver.find_element(By.ID, "answer").send_keys(func)
driver.find_element(By.ID, "solve").submit()
time.sleep(5)
