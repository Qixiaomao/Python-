import requests

req = requests.get("http://www.baidu.com")


r = req.text
print(r.encode('utf-8'))
