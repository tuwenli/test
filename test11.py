
import requests
r = requests.get("https://www.klook.com") # klook首页

r1 = requests.get('https://www.klook.com/v2/usrcsrv/component/page/home')

#print(r.status_code)
#print(r.text)
print(r1)