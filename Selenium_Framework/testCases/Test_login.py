import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_login:
    baseURL=ReadConfig.getapplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homepage(self,setup):
        self.logger.info("************ Test_001_login ******************")
        self.logger.info("************ verifying home page ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        expe_val=self.driver.title
        act_val="Your store. Login"
        if expe_val == act_val:
            assert True
            self.driver.close()
            self.logger.info("************ Home test page is passed ******************")
        else:
            self.driver.save_screenshot("Selenium_Framework\\Screenshots\\" + "test_homepage.png")
            self.driver.close()
            self.logger.info("************ Home test page is failed ******************")
            assert False

    @pytest.mark.regression
    def test_002_login(self,setup):
        self.logger.info("************ Test_002_login ******************")
        self.logger.info("************ verifying login page ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        expe_val = self.driver.title
        act_val = "Dashboard / nopCommerce administration"

        if expe_val == act_val:
            assert True
            self.driver.close()
            self.logger.info("************ login test is passed ******************")
        else:
            self.driver.save_screenshot("Selenium_Framework\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("************ login test is failed ******************")
            assert False





