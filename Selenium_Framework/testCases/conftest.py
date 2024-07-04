import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup(browser):
    global driver
    if browser == "chrome":
        serv_obj = Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=serv_obj, options=options)
        driver.implicitly_wait(10)
    elif browser == "edge":
        serv_obj = Service("C:\\Users\\svankada\\Drivers\\msedgedriver.exe")
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver = webdriver.Edge(service=serv_obj, options=options)
        driver.implicitly_wait(10)

    else: #if browser is not mentioned
        serv_obj = Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=serv_obj, options=options)
        driver.implicitly_wait(10)

    return driver

def pytest_addoption(parser): #this will get from CLI/hooks.
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

#Pytest htmal reports: #it hook for adding enviroment to html report.

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Hybrid Framework Practice'


# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Application'
#     config._metadata['Module Name'] = 'Login'
#     config._metadata['Tester'] = 'V'
#     config._metadata['Package'] = 'python'

# def pytest_configure(config):
#     config._metadata = {
#         "Project Name": "Hybrid Framework Practice",
#         "Module Name": "Customers",
#         "Tester":"Amar"
#     }

#it is hook for delete/modify enviroment to html report

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins", None)

