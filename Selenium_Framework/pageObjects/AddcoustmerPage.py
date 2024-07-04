from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys,ActionChains
import time




class AddCoustmer:
    link_coustmers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_coustmers_item_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_addnew_coustmer_xpath = "//a[normalize-space()='Add new']"
    input_email_xpath = "//input[@id='Email' and @name='Email']"
    input_password_xpath = "//input[@id='Password']"
    input_firsstname_xpath = "//input[@id='FirstName']"
    input_lastname_xpath = "//input[@id='LastName']"
    input_gender_xpath = "//div[@class='raw']/div/input"
    input_dob_xpath = "//input[@id='DateOfBirth']"
    input_ompanyname_xpath = "//input[@id='Company']"
    input_taxexempt_xpath = "//input[@id='IsTaxExempt']"
    input_newsletter_xpath = "(//span[@role='combobox'])[1]"
    input_teststore_xpath = "//li[contains(text(),'Test store 2')]"
    input_canceltrole_xpath = "//li[@class='select2-selection__choice']/span"
    input_selectgust_xpath = "//li[contains(text(),'Guests')]"
    input_admincomment_xpath = "//textarea[@id='AdminComment']"
    select_vendor_xpath = "//select[@id='VendorId']"
    select_saveclick_xpath = "//button[@name='save']"
    body_verify_tag_name = "body"


    def __init__(self,driver):
        self.driver=driver

    def getcoustmerpage(self):
        self.act = ActionChains(self.driver)
        self.menu=self.driver.find_element(By.XPATH,self.link_coustmers_menu_xpath)
        self.menu_item = self.driver.find_element(By.XPATH, self.link_coustmers_item_xpath)
        self.act.move_to_element(self.menu).click().perform()
        self.act.move_to_element(self.menu_item).click().perform()

    def AddnewCoustmer(self):
        self.driver.find_element(By.XPATH,self.link_addnew_coustmer_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.input_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.input_password_xpath).send_keys(password)

    def setFirstname(self,firsstname):
        self.driver.find_element(By.XPATH,self.input_firsstname_xpath).send_keys(firsstname)

    def setLastname(self,lastname):
        self.driver.find_element(By.XPATH,self.input_lastname_xpath).send_keys(lastname)

    def setGender(self,gender):
        self.elements=self.driver.find_elements(By.XPATH,self.input_gender_xpath)
        if gender == "Male":
            self.elements[0].click()
        elif gender == "Female":
            self.elements[1].click()
        else:
            self.elements[0].click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.input_dob_xpath).send_keys(dob)

    def setcompanyName(self,companyname):
        self.driver.find_element(By.XPATH,self.input_ompanyname_xpath).send_keys(companyname)

    def clicktaxexempt(self):
        self.driver.find_element(By.XPATH,self.input_taxexempt_xpath).click()

    def setnewSletter(self):
        self.driver.find_element(By.XPATH,self.input_newsletter_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.input_teststore_xpath).click()


    def setCoustmerrole(self):
        time.sleep(2)
        self.webels=self.driver.find_elements(By.XPATH,self.input_canceltrole_xpath)
        self.webels[1].click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.input_selectgust_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.input_admincomment_xpath).click()

    def selectvendor(self,text):
        self.vendor=Select(self.driver.find_element(By.XPATH,self.select_vendor_xpath))
        self.vendor.select_by_visible_text(text)

    def sendadmincomment(self,comment):
        self.driver.find_element(By.XPATH,self.input_admincomment_xpath).send_keys(comment)

    def saveclick(self):
        self.driver.find_element(By.XPATH,self.select_saveclick_xpath).click()

    def outputverify(self):
        self.verify=self.driver.find_element(By.TAG_NAME,self.body_verify_tag_name).text
        return self.verify






