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
investigation=InvestigationComponent.InvestigationComponent(url, cookie)

#STEP4：调用对象方法
print investigation.queryByUserName(username='Tom')
# print investigation.queryByUserName('Tom')
print investigation.queryByTaskId(taskId='528')
# print investigation.queryByTaskId('528',False)
print investigation.queryByProcessName(processName='services.exe')
# print investigation.queryByProcessName('services.exe',False)
print investigation.queryByFileName(fileName='services.exe')
# print investigation.queryByFileName('services.exe',False)
print investigation.queryByUrl(url='10.21.140.139')
# print investigation.queryByUrl('10.21.140.139',False)
print investigation.queryBySourceIp(sourceIP='10.21.140.139')
print investigation.queryBySourceIp(sourceIP='10.21.140.139',sourcePort='8080')
print investigation.queryBySourceIp(sourcePort='8080')
print investigation.queryByDestIP(desIp='10.21.140.139')
print investigation.queryByDestIP(desIp='10.21.140.139',desPort='8080')
print investigation.queryByDestIP(desPort='8080')
print investigation.queryByRegistryKey(registryKey='asdf')
print investigation.queryByRegistryValue(registryValue='2')
print investigation.queryByDefault()
print investigation.queryByDefaultAndSort(sortColumn='1',asc=False)
print investigation.queryByDefaultAndFilter(filterName="时间",filterValue="00:00:00")
print investigation.queryByDefaultAndFilter(filterName="进程用户名",filterValue="Tom")


#管理员登录创建