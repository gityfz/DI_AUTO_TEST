from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


class Browser:
    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self,url,userName,passWord):
        # profile.set_preference('webself.driver_accept_untrusted_certs',False)
        # self.driver = webself.driver.Firefox(firefox_profile=profile)
        print "111"
        self.driver.get(url)
        try:
            account = self.driver.find_element_by_id("login")
            password=self.driver.find_element_by_id("password")
            account.send_keys(userName)
            password.send_keys(passWord)
            button = self.driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/button')
            print button
            time.sleep(1)
            button.click()
            time.sleep(3)
            # self.driver.get("javascript:document.getElementById('advancedButton').click();")
            # self.driver.get("javascript:document.getElementById('exceptionDialogButton').click();")


        except NoSuchElementException:
            print "can't find seleniumhq"

    def checkCreateAdmin(self,admintype,account,password,):
        accountControl = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[6]/ul/li[1]/a')
        accountControl.click()


ll=Browser()
ll.login('https://10.21.144.81','admin','admin')
ll.checkCreateAdmin('devadmin','1234','111111')