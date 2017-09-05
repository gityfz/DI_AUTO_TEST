#!coding:utf-8
import LoginComponent
import InvestigationComponent

#STEP1:设置黑匣子服务器URL地址
url="https://10.21.144.81"
#STEP2:完成登录操作获取cookie———auth_tkt
login=LoginComponent.Login('admin', 'admin', url)
cookie=login.dologin()
print '打印cookie对象：',cookie

#STEP3:实例化新建调查对象
investigation=InvestigationComponent.newInvestigation(url, cookie)

#STEP4：调用对象方法
# print investigation.queryByUserName('Tom',True)
# print investigation.queryByUserName('Tom',False)
# print investigation.queryByTaskId('528',True)
# print investigation.queryByTaskId('528',False)
# print investigation.queryByProcessName('services.exe',True)
# print investigation.queryByProcessName('services.exe',False)
# print investigation.queryByFileName('services.exe',True)
# print investigation.queryByFileName('services.exe',False)
# print investigation.queryByUrl('10.21.140.139',True)
# print investigation.queryByUrl('10.21.140.139',False)
# print investigation.queryBySourceIp(sourceIP='10.21.140.139')
# print investigation.queryBySourceIp(sourceIP='10.21.140.139',sourcePort='8080')
# print investigation.queryBySourceIp(sourcePort='8080')
# print investigation.queryByDestIP(desIp='10.21.140.139')
# print investigation.queryByDestIP(desIp='10.21.140.139',desPort='8080')
# print investigation.queryByDestIP(desPort='8080')
# print investigation.queryByRegistryKey('asdf',True)
# print investigation.queryByRegistryValue('2',True)
# print investigation.queryByDefault()
# print investigation.queryByDefaultAndSort(sortColumn='1')
print investigation.queryByDefaultAndFilter("时间","22")


#管理员登录创建