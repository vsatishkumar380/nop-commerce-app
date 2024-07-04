import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login



class Test_001_login:
    baseURL="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"

    def test_homepage(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        expe_val=self.driver.title
        act_val="Your store" #act:Your store. Login
        if expe_val==act_val:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("Selenium_Framework\\Screenshots\\"+"test_homepage.png")
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        expe_val = self.driver.title
        act_val = "Dashboard / nopCommerce administration_12345" #act:"Dashboard / nopCommerce administration"


        if expe_val == act_val:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("Selenium_Framework\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False





