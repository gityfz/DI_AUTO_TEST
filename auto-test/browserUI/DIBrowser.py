# coding=utf-8
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from InterfaceUI import ParamsUtil
from InterfaceUI import DiErrorUtil



class Browser:
    def __init__(self,url,account,password):
        self.driver=webdriver.Chrome()
        self.url=url
        self.account=account
        self.password=password

    def login(self):
        # profile.set_preference('webself.driver_accept_untrusted_certs',False)
        # self.driver = webself.driver.Firefox(firefox_profile=profile)
        self.driver.get(self.url)
        self.driver.maximize_window()
        try:
            account = self.driver.find_element_by_id("login")
            password=self.driver.find_element_by_id("password")
            account.send_keys(self.account)
            password.send_keys(self.password)
            button = self.driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/button')
            time.sleep(1)
            button.click()
            time.sleep(4)
            # self.driver.get("javascript:document.getElementById('advancedButton').click();")
            # self.driver.get("javascript:document.getElementById('exceptionDialogButton').click();")
        except NoSuchElementException,e:
            print e
        else:
            print '登陆成功'
            return True

    def checkCreateAdmin(self,admintype,account,password):
        if(ParamsUtil.isString(account) and ParamsUtil.isPassword(password)):
            pass
        else:
            raise DiErrorUtil.ParamsError(msg='用户名密码参数错误')
        if( ParamsUtil.isAId(admintype)==False or int(admintype)<1 or int(admintype)>3):
            raise DiErrorUtil.ParamsError(msg='管理员类型错误')
        systemControl=self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[6]/a')
        systemControl.click()
        time.sleep(0.2)
        accountControl = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[6]/ul/li[1]/a')
        accountControl.click()
        time.sleep(0.2)
        try:
            texts = self.driver.find_elements_by_xpath('//span')
            for text in texts:
                if (text.text == account):
                    raise DiErrorUtil.ParamsError(msg='用户名已经存在')
        except NoSuchElementException,e:
            pass
        #新增用户
        createAdmin=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/div[2]/button[1]')
        createAdmin.click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="newaccountform"]/div[1]/div/select').click()
        time.sleep(0.2)
        if(admintype=='1'):
            self.driver.find_element_by_xpath('//*[@id="newaccountform"]/div[1]/div/select/option[1]').click()
        elif(admintype=='2'):
            self.driver.find_element_by_xpath('//*[@id="newaccountform"]/div[1]/div/select/option[2]').click()
        else:
            self.driver.find_element_by_xpath('//*[@id="newaccountform"]/div[1]/div/select/option[3]').click()
        #键入账号
        self.driver.find_element_by_xpath('//*[@id="newaccountform"]/div[2]/div/input').send_keys(account)
        #键入密码
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        #键入描述
        self.driver.find_element_by_xpath('//*[@id="newaccountform"]/div[3]/div/textarea').send_keys('miaoshu')
        #键入密码确认并回车
        self.driver.find_element_by_xpath('//*[@id="newaccountform"]/div[5]/div/input').send_keys(password+Keys.RETURN)
        time.sleep(0.5)
        try:
            texts = self.driver.find_elements_by_xpath('//span')
            for text in texts:
                if(text.text==account):
                    print '创建用户成功'
                    return True
        except NoSuchElementException,e:
            print e


    def checkDefaultNewInvestigation(self):
        time.sleep(0.5)
        #进入新建调查页
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/ul/li[1]/a').click()
        time.sleep(5)
        #搜索
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[4]/button[1]').click()
        time.sleep(15)

        #获取表单数据条数
        try:
            text=self.driver.find_element_by_xpath('//*[@id="search-result_info"]')
        except NoSuchElementException:
            print '结果没有成功返回'
            return False
        else:
            print '新建调查界面默认条件搜索成功反正结果，页面显示情况为：',text.text
            strout = text.text.encode("utf-8")
            startIndex = 7
            endIndex = strout.find('条') - 1
            result = int(strout[startIndex:endIndex].replace(',', ''))
            # print result
            return result

    def checkNewInvestigationByFileName(self,filename):
        methodName = sys._getframe().f_code.co_name
        if(ParamsUtil.isString(filename)==False):
            raise DiErrorUtil.ParamsError(methodName=methodName,msg='参数错误')
        time.sleep(0.5)
        # 进入新建调查页
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/ul/li[1]/a').click()
        time.sleep(5)

        # 选中前一天
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/button').click()
        self.driver.find_element_by_xpath('//*[@id="self-time"]').click()
        self.driver.find_element_by_xpath('//td[@class="day today"]/preceding-sibling::td[1]').click()
        time.sleep(1)

        # 输入文件名
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/button').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="ui-select-choices-row-0-3"]/span').click()
        time.sleep(0.2)
        filenameInput=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div[5]/input')
        filenameInput.send_keys(filename)
        time.sleep(1)
        # 执行搜索
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[4]/button[1]').click()
        time.sleep(15)
        try:
            text=self.driver.find_element_by_xpath('//*[@id="search-result_info"]')
        except NoSuchElementException:
            print '结果没有成功返回'
            return False
        else:
            print '新建调查界面按照“文件名”检索成功返回，页面显示情况为：',text.text
            print '检索时间范围为前一天的0点到当前的时间'
            strout = text.text.encode("utf-8")
            startIndex=7
            endIndex=strout.find('条')-1
            result=int(strout[startIndex:endIndex].replace(',',''))
            # print result
            return result

    def checkSaveSearchRules(self,ruleName):
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isString(ruleName) == False):
            raise DiErrorUtil.ParamsError(methodName=methodName, msg='参数错误')
        time.sleep(0.5)
        # 进入新建调查页
        if(self.checkDefaultNewInvestigation()==False):
            return False

        time.sleep(5)
        #保存规则
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[4]/button[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[2]/input').send_keys(ruleName)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[3]/button[1]').click()

        # 进入调查记录页
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/ul/li[2]/a').click()
        time.sleep(1)

        try:
            text=self.driver.find_element_by_xpath('//*[@id="investigation"]/tbody/tr[2]/td[4]/a')
        except NoSuchElementException:
            print '调查规则没有保存成功'
            return False
        else:
            if(text.text==ruleName):
                print '调查规则成功保存'
                return True
            else:
                print '调查规则没有成功保存'
                return False

    def gotoTreePage(self):
        if(self.checkDefaultNewInvestigation()==False):
            return False
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="search-result"]/tbody/tr[1]/td[5]/a').click()
        time.sleep(10)


    def checkSaveTreeRules(self,ruleName):
        methodName = sys._getframe().f_code.co_name
        if(ParamsUtil.isString(ruleName)==False):
            raise DiErrorUtil.ParamsError(methodName=methodName, msg='参数错误')
        if(self.gotoTreePage()==False):
            return False
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div/div[2]/div[1]/button[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/input').send_keys(ruleName)
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/button[1]').click()
        print '完成事件树规则保存'
        # 进入调查记录——历史事件树页
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/ul/li[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[2]/div/ul/li[2]').click()
        time.sleep(5)
        try:
            text = self.driver.find_element_by_xpath('//*[@id="13"]/td[4]/a')
        except NoSuchElementException:
            print '事件树规则没有保存成功'
            return False
        else:
            if(text.text.find(ruleName)==-1):
                print '事件树规则没有保存成功'
                return False
            else:
                print '事件树规则保存成功'
                return False
        finally:
            self.driver.close()



