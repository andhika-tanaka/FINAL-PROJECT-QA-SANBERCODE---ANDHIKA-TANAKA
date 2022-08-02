import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class OrangeHRMLogin (unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.dashboardUrl = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
        self.loginUrl = "https://opensource-demo.orangehrmlive.com/"
        
    def test_a_check_login_page (self):
        driver = self.driver
        driver.get(self.loginUrl)

        self.assertIn(driver.title, "OrangeHRM")
        expectedUrl= driver.current_url
        self.assertEqual(self.loginUrl, expectedUrl)
        
    def test_b_login_with_valid_data(self):
        driver = self.driver
        driver.get(self.loginUrl)
        
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.ID, "txtPassword")
        btnSubmit = driver.find_element(By.ID, "btnLogin")

        username.send_keys("admin")
        password.send_keys("admin123")
        btnSubmit.click()
        
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != self.loginUrl)

        expectedUrl= driver.current_url
        self.assertEqual(self.dashboardUrl, expectedUrl)

    def test_c_login_with_invalid_username(self):
        driver = self.driver
        driver.get(self.loginUrl)
        
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.ID, "txtPassword")
        btnSubmit = driver.find_element(By.ID, "btnLogin")

        username.send_keys("falseadmin")
        password.send_keys("admin123")
        btnSubmit.click()
        time.sleep(5)

        errMessage = driver.find_element(By.ID, "spanMessage").text
        expectedMessage = "Invalid credentials"
        self.assertEqual(errMessage, expectedMessage)

    def test_d_login_with_invalid_password(self):
        driver = self.driver
        driver.get(self.loginUrl)
        
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.ID, "txtPassword")
        btnSubmit = driver.find_element(By.ID, "btnLogin")

        username.send_keys("admin")
        password.send_keys("admin456")
        btnSubmit.click()
        time.sleep(5)

        errMessage = driver.find_element(By.ID, "spanMessage").text
        expectedMessage = "Invalid credentials"
        self.assertEqual(errMessage, expectedMessage)
    
    def test_e_login_with_empty_username(self):
        driver = self.driver
        driver.get(self.loginUrl)
        
        username = driver.find_element(By.ID, "txtUsername")
        btnSubmit = driver.find_element(By.ID, "btnLogin")

        btnSubmit.click()
        time.sleep(5)

        nullUsernameMessage = driver.find_element(By.ID, "spanMessage").text
        
        expectedNullUsernameMessage = "Username cannot be empty"

        self.assertEqual(username.text, "")
        self.assertEqual(nullUsernameMessage, expectedNullUsernameMessage)

    def test_f_login_with_empty_password(self):
        driver = self.driver
        driver.get(self.loginUrl)
        
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.ID, "txtPassword")
        btnSubmit = driver.find_element(By.ID, "btnLogin")

        username.send_keys("admin")
        btnSubmit.click()
        time.sleep(5)

        nullPasswordMessage = driver.find_element(By.ID, "spanMessage").text
        
        expectedNullPasswordMessage = "Password cannot be empty"

        self.assertEqual(password.text, "")
        self.assertEqual(nullPasswordMessage, expectedNullPasswordMessage)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()