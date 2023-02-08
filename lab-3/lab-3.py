import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import choice
import string


def generate_email():
    email = ""
    for _ in range(10):
        email += choice(string.ascii_lowercase)
    email += "@mail.com"
    return email


class TestPage(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_registration(self):
        self.driver.get("http://demo-store.seleniumacademy.com/customer/account/create/")
        first_name = "Automation"
        middle_name = "Testing"
        last_name = "Course"
        email = generate_email()
        password = "auto-test1ng3-site"
        self.driver.find_element(By.XPATH, '//*[@id="firstname"]').send_keys(first_name)
        self.driver.find_element(By.XPATH, '//*[@id="middlename"]').send_keys(middle_name)
        self.driver.find_element(By.XPATH, '//*[@id="lastname"]').send_keys(last_name)
        self.driver.find_element(By.XPATH, '//*[@id="email_address"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="confirmation"]').send_keys(password)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button').submit()
        time.sleep(5)
        real = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div/ul/li/ul/li/span').text
        expected = "Thank you for registering with Madison Island."
        self.assertEqual(real, expected)

    def test_filter(self):
        self.driver.get("http://demo-store.seleniumacademy.com/")
        self.driver.find_element(By.ID, 'search').send_keys('men')
        self.driver.implicitly_wait(2)
        real = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[4]/form/div[2]/ul').size
        expected = {'height': 379, 'width': 300}
        self.assertEqual(real, expected)
        time.sleep(3)
        self.driver.get("http://demo-store.seleniumacademy.com/women/new-arrivals.html")
        self.driver.implicitly_wait(2)
        real = self.driver.find_element(By.CSS_SELECTOR, 'li.item:nth-child(1) > div:nth-child(2) > h2:nth-child(1)').text
        expected = 'Elizabeth Knit Top'.upper()
        self.assertEqual(real, expected)

    def test_cart_adding(self):
        self.driver.get('http://demo-store.seleniumacademy.com/accessories/jewelry.html')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/button/span/span').click()
        time.sleep(2)
        real = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/ul/li/ul/li/span').text
        time.sleep(2)
        expected = 'was added to your shopping cart.'
        self.assertIn(expected, real)

    @classmethod
    def tearDown(cls) -> None:
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
