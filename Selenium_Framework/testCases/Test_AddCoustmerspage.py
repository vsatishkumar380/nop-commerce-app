import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.AddcoustmerPage import AddCoustmer
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
    def test_002_login(self,setup):
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
        self.ac.AddnewCoustmer()
        self.logger.info("************ Add new is successful******************")

        self.logger.info("************ providing coustmer info.******************")
        self.Email = random_generator() + "@yourstore.com"
        self.ac.setEmail(self.Email)
        self.ac.setPassword("test123")
        self.ac.setFirstname("ramudu")
        self.ac.setLastname("kalki")
        self.ac.setGender("Female")
        self.ac.setDOB("19-01-1991")
        self.ac.setcompanyName("selenium_python")
        self.ac.clicktaxexempt()
        self.ac.setnewSletter()
        self.ac.setCoustmerrole()
        self.ac.selectvendor("Vendor 1")
        self.ac.sendadmincomment("please add my account")
        self.ac.saveclick()
        self.logger.info("************ provided the coustmer info.******************")
        self.msg = self.ac.outputverify()
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("************ Test Case is passed******************")

        else:
            self.driver.save_screenshot("Selenium_Framework/Screenshots" + "Addcoustomer.png")
            assert True == False
            self.logger.info("************ Test Case is failed.******************")

        self.driver.close()
        self.logger.info("************ Ended.******************")
