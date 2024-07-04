import configparser
config=configparser.RawConfigParser()
config.read("Selenium_Framework\\Confugurations\\config.ini") # use this also : ".\\Confugurations\\config.ini" ==> not working.

class ReadConfig():
    @staticmethod
    def getapplicationURL():
        url=config.get("common_info","baseURL")
        return url

    @staticmethod
    def getUserName():
        username = config.get("common_info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common_info", "password")
        return password

class datadriveConfig():

    @staticmethod
    def getapplicationURL():
        url = config.get("data_driven", "baseURL")
        return url

    @staticmethod
    def getPath():
        username = config.get("data_driven", "path")
        return username

