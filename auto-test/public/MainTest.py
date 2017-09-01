import LoginComponent
import InvestigationComponent


url="https://10.21.144.81"
login=LoginComponent.Login('admin', 'admin', url)
cookie=login.dologin()
print cookie
investigation=InvestigationComponent.newInvestigation(url, cookie)
print investigation.queryByUserName('tom',22)