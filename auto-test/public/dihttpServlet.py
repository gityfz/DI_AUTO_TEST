import diurlerror
import ssl
import urllib2

class Servlet(object):


    def __init__(self):
        self.url=''
        self.data=''


    def doPost(self,url,data,cookie):
        ssl._create_default_https_context = ssl._create_unverified_context
        cookiehand = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(urllib2.HTTPRedirectHandler(), cookiehand)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        try:
            if(data):
                response = opener.open(fullurl=url,data=data)
            else:
                response = opener.open(fullurl=url)
        except urllib2.HTTPError,e:
            diurlerror.printError(e)
        else:
            return response

    def doGet(self,url,cookie):
        Servlet.doPost(self,url=url,data=None,cookie=cookie)