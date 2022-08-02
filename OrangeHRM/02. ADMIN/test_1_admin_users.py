import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class OrangeHRMAdminUsers (unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.dashboardUrl = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
        self.loginUrl = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
        self.usersUrl = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        
    def user_login(self):
        driver = self.driver
        driver.get(self.loginUrl)
        
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.ID, "txtPassword")
        btnLogin = driver.find_element(By.ID, "btnLogin")

        username.send_keys("admin")
        password.send_keys("admin123")
        btnLogin.click()
        time.sleep(3)

        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != self.dashboardUrl)

    def test_a_check_admin_users_page (self):
        self.user_login()
        
        driver = self.driver
        
        subMenuUsers = driver.find_element(By.ID, "")

        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != self.loginUrl)

        self.assertIn(driver.title, "OrangeHRM")
        expectedUrl= driver.current_url
        self.assertEqual(self.usersUrl, expectedUrl)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()