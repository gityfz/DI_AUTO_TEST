import autoLogin
import NewInvestigation


url="https://10.21.144.81"
login=autoLogin.Login('admin','admin',url)
cookie=login.dologin()
print cookie
investigation=NewInvestigation.newInvestigation(url,cookie)
investigation.queryByUserName('tom',contains=False)