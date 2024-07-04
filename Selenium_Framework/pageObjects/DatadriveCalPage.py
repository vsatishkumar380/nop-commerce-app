from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys,ActionChains



class Cal:
    input_principle_xpath="//input[@id='principal']"
    input_interest_xpath="//input[@id='interest']"
    input_tenure_xpath = "//input[@id='tenure']"
    input_tenurePeriod_xpath = "//select[@id='tenurePeriod']"
    input_frequency_xpath = "//select[@id='frequency']"
    button_calculate_xpath = "//div[@class='CTR PT15']/a[1]"
    strong_maturityval_xpath = "//span[@id='resp_matval']/strong"
    button_clear_xpath = "//div[@class='CTR PT15']/a[2]"

    def __init__(self,driver):
        self.driver=driver

    def setprinciple(self,principle):
        self.driver.find_element(By.XPATH,self.input_principle_xpath).send_keys(principle)

    def setinterest(self,interest):
        self.driver.find_element(By.XPATH,self.input_interest_xpath).send_keys(interest)

    def settenure(self,tenure):
        self.driver.find_element(By.XPATH,self.input_tenure_xpath).send_keys(tenure)

    def settenurePeriod(self,tenurePeriod):
        self.tenperiod = Select(self.driver.find_element(By.XPATH, self.input_tenurePeriod_xpath))
        self.tenperiod.select_by_visible_text(tenurePeriod)


    def setfrequence(self,frequence):
        self.freq = Select(self.driver.find_element(By.XPATH, self.input_frequency_xpath))
        self.freq.select_by_visible_text(frequence)

    def clickcalculate(self):
        self.driver.find_element(By.XPATH,self.button_calculate_xpath).click()

    def getmaturityval(self):
        self.actuval_Mvalue=self.driver.find_element(By.XPATH,self.strong_maturityval_xpath).text
        return self.actuval_Mvalue

    def clickclear(self):
        self.driver.find_element(By.XPATH,self.button_clear_xpath).click()







