#!coding:utf-8
import re
import diurlerror
import ssl
import urllib2
import urllib
import socket
import cookielib

##
##完成登录请求,并保存登录信息
##

class HttpRedirect2_Handler(urllib2.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        print '进入302重定向'
        pass

class Login(object):
    def __init__(self,account,password,url=None):
        self.account=account
        self.password=password
        localIP = 'https://' + socket.gethostbyname(socket.gethostname())
        if (url == None):
            self.url =localIP
            print 'targer url is:',self.url
        else:
            regex = re.compile(r'^(?:http|ftp)s?://'  # http:// or https://
                , re.IGNORECASE)
            if(regex.match(url)):
                self.url=url
                print 'targer url is:',self.url
            else:
                self.url=''


    def  dologin(self):
        # 取消SSL证书校验
        ssl._create_default_https_context = ssl._create_unverified_context
        data = {
                'came_from':self.url,
                'login': self.account,
                'form.submitted':'',
                'password': self.password,
                }
        data = urllib.urlencode(data)
        cookie = cookielib.CookieJar()
        cookiehand = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(HttpRedirect2_Handler(),cookiehand)
        opener_normal=urllib2.build_opener(urllib2.HTTPRedirectHandler(),cookiehand)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        try:
            if(self.url==''):
                print 'url格式错误'
                return
            # req = urllib2.Request(url=self.url,headers=self.send_headers, data=self.data)

            response=opener.open(fullurl=self.url+'/login',data=data)
            # response=urllib2.urlopen(req,context=context)
            print response.code
        except urllib2.HTTPError,e:
            diurlerror.printError(e)
            try:
                opener_normal.open(fullurl=self.url,data=data)
            except urllib2.HTTPError,e:
                diurlerror.printError(e)
            except urllib2.URLError, e:
                diurlerror.printError(e)
            else:
                # print response.read()
                return cookie
        except urllib2.URLError, e:
            diurlerror.printError(e)
        else:
            return cookie

