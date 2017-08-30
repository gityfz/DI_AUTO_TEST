import autoLogin
login=autoLogin.Login('admin','admin',"https://10.21.137.163")
cookie=login.dologin()
print cookie
