from multiprocessing.connection import wait
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class OrangeHRMAdminUsers (unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.dashboardUrl = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
        self.loginUrl = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
        self.buzzUrl = "https://opensource-demo.orangehrmlive.com/index.php/directory/viewDirectory/reset/1"
        
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
        wait.until(lambda driver: driver.current_url != self.loginUrl)
        
    def directory_page(self):
        driver = self.driver
        action = ActionChains(driver)
        
        self.user_login()

        menuDirectory = driver.find_element(By.XPATH, "//b[normalize-space()='Directory']")

        action.move_to_element(menuDirectory).click().perform()

    def test_a_check_directory_page (self): 
        driver = self.driver

        self.directory_page()

        directoryTitlePage = driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div[1]/h1").text
        self.assertIn("Search Directory", directoryTitlePage)
        expectedUrl= driver.current_url
        self.assertIn(expectedUrl, self.buzzUrl)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()