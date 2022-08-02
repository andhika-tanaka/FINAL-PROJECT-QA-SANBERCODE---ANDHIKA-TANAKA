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
        self.employeetimesheetsUrl = "https://opensource-demo.orangehrmlive.com/index.php/time/viewEmployeeTimesheet"
        
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
        
    def employee_timer_page(self):
        driver = self.driver
        action = ActionChains(driver)
        
        self.user_login()

        menuTime = driver.find_element(By.XPATH, "//b[normalize-space()='Time']")
        submenuTimeSheets = driver.find_element(By.XPATH, "//a[@id='menu_time_Timesheets']")
        submenuEmployeeTimesheets = driver.find_element(By.XPATH, "//a[@id='menu_time_viewEmployeeTimesheet']")

        action.move_to_element(menuTime).perform()
        action.move_to_element(submenuTimeSheets).perform()
        action.move_to_element(submenuEmployeeTimesheets).click().perform()

    def test_a_check_employee_timer_page (self): 
        driver = self.driver

        self.employee_timer_page()

        employeetimesheetsTitlePage = driver.find_element(By.XPATH, "//h1[normalize-space()='Timesheets Pending Action']").text
        self.assertIn("Timesheets Pending Action", employeetimesheetsTitlePage)
        expectedUrl= driver.current_url
        self.assertIn(expectedUrl, self.employeetimesheetsUrl)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()