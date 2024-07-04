from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys,ActionChains
import time


class SearchCoustmer:
    input_SearchEmail_xpath = "//input[@id='SearchEmail']"
    input_SearchFirstName_xpath = "//input[@id='SearchFirstName']"
    button_Searchclick_xpath = "//button[@id='search-customers']"
    table_TableRows_xpath = "//div[@class='dataTables_scrollBody']/table/tbody/tr"
    input_SearchFirstName_xpath = "//input[@id='SearchFirstName']"
    input_SearchLastName_xpath = "//input[@id='SearchLastName']"




    def __init__(self,driver):
        self.driver=driver

    def SearchEmail(self,Email):
        self.driver.find_element(By.XPATH, self.input_SearchEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_SearchEmail_xpath).send_keys(Email)

    def SearchFirstName(self,FirstName):
        self.driver.find_element(By.XPATH, self.input_SearchFirstName_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_SearchFirstName_xpath).send_keys(FirstName)

    def Searchclick(self):
        self.driver.find_element(By.XPATH, self.button_Searchclick_xpath).click()

    def TableRows(self):
        self.rows=self.driver.find_elements(By.XPATH, self.table_TableRows_xpath)
        return len(self.rows)

    def SearchbyEmail(self,email):
        flag=False
        for r in range(1,self.TableRows()+1):
            self.emailid=self.driver.find_element(By.XPATH, "//div[@class='dataTables_scrollBody']/table/tbody/tr["+str(r)+"]/td[2]").text
            if self.emailid==email:
                flag = True
                break
        return flag

    def SearchbyName(self,name):
        flag=False
        for r in range(1,self.TableRows()+1):
            self.nameid=self.driver.find_element(By.XPATH, "//div[@class='dataTables_scrollBody']/table/tbody/tr["+str(r)+"]/td[3]").text
            if self.nameid==name:
                flag = True
                break
        return flag


    def SearchFirstName(self,FirstName):
        self.driver.find_element(By.XPATH, self.input_SearchFirstName_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_SearchFirstName_xpath).send_keys(FirstName)

    def SearchLastName(self,LastName):
        self.driver.find_element(By.XPATH, self.input_SearchLastName_xpath).clear()
        self.driver.find_element(By.XPATH,self.input_SearchLastName_xpath).send_keys(LastName)




