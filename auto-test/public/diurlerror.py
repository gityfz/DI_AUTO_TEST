#!coding:utf-8
def printError(e):
    if(e==None):
        return
    if hasattr(e, 'code'):
        if(str(e).find('302')):
            print '服务器登录成功，正在重定向到首页...---->'
        elif(str(e).find('401')):
            print 'session过期导致账号已登出或用户名码错误,请重新登录'
            print '错误码为: ', e.code
        else:
            print '服务器无法完成请求。'
            print '错误码为: ', e.code