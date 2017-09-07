# coding=utf-8
import DIBrowser

##
 #    浏览器端UI验证流程
 #    注：默认在新建调查页面等待15秒，若网络较慢，15s还没有加载页面，会抛出异常
 #    可以再次运行脚本或者增加等待时间
##


#STEP1 :实例化浏览器驱动对象，传入黑匣子ip以及登录的用户名密码
browser=DIBrowser.Browser(url='https://10.21.144.81',account='admin',password='admin')
#STEP2 :进行登录操作
browser.login()
#STEP3 :进入账户管理页面，新建一个用户,1,2,3分别对应3种管理员类型，并传入账号密码，若账号已经存在，则抛出异常
browser.checkCreateAdmin(admintype='1',account='12345678',password='111111')
#STEP4 :进入新建调查页面，根据文件名检索结果
browser.checkNewInvestigationByFileName(filename='1')
#STEP5 :进入新建调查页面，根据默认条件检索结果，并保存规则，查看规则是否保存成功
browser.checkSaveSearchRules(ruleName='asdf')
#STEP6 :进入新建调查页面，根据默认条件检索结果，并点击第一条记录的进程id进入事件树查看，保存事件树的规则，并查看是否保存成功
browser.checkSaveTreeRules(ruleName='asdf')