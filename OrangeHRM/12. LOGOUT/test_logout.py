import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class OrangeHRMLogout (unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.dashboardUrl = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
        self.loginUrl = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
        
    def test_a_check_logout_function (self):
        driver = self.driver
        driver.get(self.loginUrl)
        
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.ID, "txtPassword")
        btnLogin = driver.find_element(By.ID, "btnLogin")

        username.send_keys("admin")
        password.send_keys("admin123")
        btnLogin.click()
        time.sleep(3)

        welcome = driver.find_element(By.ID, "welcome")
        btnLogout = driver.find_element(By.XPATH, "//*[@id='welcome-menu']/ul/li[3]/a")

        welcome.click()
        time.sleep(3)
        btnLogout.click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != self.dashboardUrl)

        self.assertIn(driver.title, "OrangeHRM")
        expectedUrl= driver.current_url
        self.assertEqual(self.loginUrl, expectedUrl)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()