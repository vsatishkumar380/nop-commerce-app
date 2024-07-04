import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.AddcoustmerPage import AddCoustmer
from pageObjects.SearchCoustmerPage import SearchCoustmer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver import Keys,ActionChains
import random
import string



def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Test_addcoustmerpage:
    baseURL=ReadConfig.getapplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_searchbyEmail_login(self,setup):
        self.logger.info("************ addcoustmerpage ******************")
        self.logger.info("************ verifying login page ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("************ login is successful/you are in dashboard ******************")
        self.logger.info("************ moving to coustermer page ******************")
        self.ac = AddCoustmer(self.driver)
        self.ac.getcoustmerpage()
        self.logger.info("************ customer page is successful******************")
        self.logger.info("************ search by Email.******************")
        self.searchcust = SearchCoustmer(self.driver)
        self.searchcust.SearchEmail("kiyjcycyhjc676008@gmail.com")
        self.searchcust.Searchclick()
        self.logger.info("************ Validation.******************")
        self.status=self.searchcust.SearchbyEmail("kiyjcycyhjc676008@gmail.com")
        if self.status==True:
            assert True==True
            self.logger.info("************ Test Case passed******************")
        else:
            self.driver.save_screenshot("Selenium_Framework\\Screenshots" + "\\searchbyEmail.png")
            assert True == False
            self.logger.info("************ Test Case failed******************")

        self.driver.close()

    @pytest.mark.sanity
    def test_searchbyName_login(self,setup):
        self.logger.info("************ addcoustmerpage ******************")
        self.logger.info("************ verifying login page ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("************ login is successful/you are in dashboard ******************")
        self.logger.info("************ moving to coustermer page ******************")
        self.ac = AddCoustmer(self.driver)
        self.ac.getcoustmerpage()
        self.logger.info("************ customer page is successful******************")
        self.logger.info("************ search by Name.******************")
        self.searchcust = SearchCoustmer(self.driver)
        self.searchcust.SearchFirstName("Virat")
        self.searchcust.SearchLastName("Kohli")
        self.searchcust.Searchclick()
        self.logger.info("************ Validation.******************")
        self.status=self.searchcust.SearchbyName("Virat Kohli")
        if self.status==True:
            assert True==True
            self.logger.info("************ Test Case passed******************")
        else:
            self.driver.save_screenshot(
                "\\Selenium_Framework\\Screenshots" + "\\searchbyName.png")
            assert True == False
            self.logger.info("************ Test Case failed******************")

        self.driver.close()












        










