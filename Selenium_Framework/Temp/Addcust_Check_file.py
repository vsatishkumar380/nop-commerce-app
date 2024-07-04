import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys,ActionChains

serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

#login
userName=driver.find_element(By.XPATH,"//input[@id='Email']")
userName.clear()
userName.send_keys("admin@yourstore.com")
Password=driver.find_element(By.XPATH,"//input[@id='Password']")
Password.clear()
Password.send_keys("admin")
driver.find_element(By.XPATH,"//button[@class='button-1 login-button']").click()

#move to customer:
customer_widj=driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]")
customer_widj2=driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")

act=ActionChains(driver)
act.move_to_element(customer_widj).click().perform()
act.move_to_element(customer_widj2).click().perform()
# print(driver.title)




#//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]
# /html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p
#//li[@class='nav-item has-treeview menu-open']/ul/li[1]

#click on add new:
driver.find_element(By.XPATH,"//a[normalize-space()='Add new']").click()
act_title="Add a new customer / nopCommerce administration"
exp_title=driver.title


driver.find_element(By.XPATH,"//input[@id='Email' and @name='Email']").send_keys("admin1@yourstore.com")
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin1")
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Satheesh")
driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("vankadaru")
checkbox=driver.find_elements(By.XPATH,"//div[@class='raw']/div/input")
checkbox[0].click()
driver.find_element(By.XPATH,"//input[@id='DateOfBirth']").send_keys("19-01-1991")
driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("Robot_selenium")
driver.find_element(By.XPATH,"//input[@id='IsTaxExempt']").click()


# time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/span").click()
lstitem=driver.find_element(By.XPATH,"//li[contains(text(),'Test store 2')]")
time.sleep(3)
lstitem.click()
time.sleep(3)
elemts=driver.find_elements(By.XPATH,"//li[@class='select2-selection__choice']/span")
elemts[1].click()
time.sleep(2)
driver.find_element(By.XPATH,"//li[contains(text(),'Guests')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//ul[@class='select2-selection__rendered'])[2]").click()

time.sleep(3)
vendor=Select(driver.find_element(By.XPATH,"//select[@id='VendorId']"))
vendor.select_by_visible_text("Vendor 1")


driver.find_element(By.XPATH,"//textarea[@id='AdminComment']").send_keys("Plaese aprrove")
time.sleep(5)

driver.find_element(By.XPATH,"//button[@name='save']").click()
time.sleep(3)

verify=driver.find_element(By.TAG_NAME,"body").text

if "The new customer has been added successfully." in verify:
    print("Test Case is passed")




#driver.execute_script("arguments[0].click();",lstitem)


# newssettler=driver.find_elements(By.XPATH,"//span[@class='select2-results']/ul/li")
# newssettler[0].click()










