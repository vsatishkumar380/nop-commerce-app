import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.DatadriveCalPage import Cal
from utilities.readProperties import datadriveConfig
from utilities.customLogger import LogGen
from utilities import XLUtill
import openpyxl


import time



class Test_001_cal:
    baseURL=datadriveConfig.getapplicationURL()
    path=datadriveConfig.getPath()

    logger=LogGen.loggen()

    @pytest.mark.other
    def test_001_cal(self,setup):
        self.logger.info("************ Test_001_cal ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Cal(self.driver)

        self.row=XLUtill.getRowCount(self.path,"Sheet1")
        print("No of rows in Excel:",self.row)
        lst = []
        for r in range(2,self.row+1):
            self.principle = XLUtill.readData(self.path, "Sheet1", r, 1)
            self.interest = XLUtill.readData(self.path, "Sheet1", r, 2)
            self.tenure = XLUtill.readData(self.path, "Sheet1", r, 3)
            self.tenurePeriod = XLUtill.readData(self.path, "Sheet1", r, 4)
            self.frequence = XLUtill.readData(self.path, "Sheet1", r, 5)
            self.expect_Mvalue = XLUtill.readData(self.path, "Sheet1", r, 6)
            print(self.principle, self.interest, self.tenure, self.tenurePeriod, self.frequence, self.expect_Mvalue)
            #calling the methods.
            self.lp.setprinciple(self.principle)
            self.lp.setinterest(self.interest)
            self.lp.settenure(self.tenure)
            self.lp.settenurePeriod(self.tenurePeriod)
            self.lp.setfrequence(self.frequence)
            self.lp.clickcalculate()

            self.actuval_Mvalue=self.lp.getmaturityval()
            print(self.actuval_Mvalue)
            print(self.expect_Mvalue)

            if float(self.expect_Mvalue) == float(self.actuval_Mvalue):
                print("Pass")
                lst.append("Pass")
            else:
                print("fail")

                lst.append("fail")

            self.lp.clickclear()

        self.driver.close()
        print(lst)

        if lst==['Pass', 'Pass', 'Pass', 'Pass', 'fail']:
            print("Total test passed")
        else:
            print("Total test Failed.")
















