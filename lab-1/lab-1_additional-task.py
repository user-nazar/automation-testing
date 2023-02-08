import time
from selenium import webdriver
from selenium.webdriver.common.by import By


WEBSITE_PATH_1 = 'http://demo-store.seleniumacademy.com/customer/account/create/'
WEBSITE_PATH_2 = 'https://www.instagram.com/maria__bnd/'

# Open web page
driver = webdriver.Chrome()
driver.get(WEBSITE_PATH_2)
time.sleep(7)
driver.get(WEBSITE_PATH_1)

user_information = {
    'first_name': 'Maria',
    'last_name': 'Bunda',
    'email_address': 'maria.bunda.student.course5@lpnu.ua',
    'password': 'secret_key',
}

# Fill in personal data
first_name_input_element = driver.find_element(By.XPATH, "//input[@name='firstname']")
first_name_input_element.send_keys(user_information.get('first_name'))

last_name_input_element = driver.find_element(By.XPATH, "//input[@id='lastname']")
last_name_input_element.send_keys(user_information.get('last_name'))

email_address_input_element = driver.find_element(By.XPATH, "//input[@type='email']")
email_address_input_element.send_keys(user_information.get('email_address'))

password_input_element = driver.find_element(By.XPATH, "//input[@title='Password']")
password_input_element.send_keys(user_information.get('password'))

confirm_password_input_element = driver.find_element(By.XPATH, "//input[@id='confirmation']")
confirm_password_input_element.send_keys(user_information.get('password'))

# Click the "Sign Up for Newsletter" checkbox
subscribe_checkbox_element = driver.find_element(By.XPATH, "//input[@id='is_subscribed']")
subscribe_checkbox_element.click()
time.sleep(3)

# Press the 'Register' button
register_button_element = driver.find_element(By.XPATH, "//button[@title='Register']")
register_button_element.click()
time.sleep(5)

driver.quit()