import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Test_001_login:
    baseURL="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"

    def test_homepage(self,):
        self.serv_obj = Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=self.serv_obj, options=options)
        self.driver.get(self.baseURL)


#for fixtures.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import smtplib


@pytest.fixture
def setup():
    global driver
    serv_obj = Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=serv_obj, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver



#Total test:
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  pageObjects.LoginPage import Login


@pytest.fixture
def setup():
    global driver
    serv_obj = Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=serv_obj, options=options)
    return driver


class Test_001_login:
    baseURL="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"

    def test_homepage(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.driver.close()

from  pageObjects.LoginPage import Login


#logging data Not working below

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="Selenium_Framework\\Logs\\Automation.log",
                            format= '%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger