from selenium.webdriver.common.by import By

class Login:
    input_username_id="Email"
    input_password_id="Password"
    button_login_xpath="//button[@class='button-1 login-button']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.input_username_id).clear()
        self.driver.find_element(By.ID,self.input_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID, self.input_password_id).clear()
        self.driver.find_element(By.ID,self.input_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_linktext).click()

