# 文件上传
import requests

# files = {'file':open('favicon.ico','rb')}
# r =requests.post('http://httpbin.org/post',files=files)
# print(r.text)

# # Cookies
# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+ value)

# 会话维持

# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)

'''
直接用以上的方法没办法获取到cookies，则意味着不能维持会话
{
  "cookies": {}
}
'''

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/1232456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


'''
这样就有cookies值
{
  "cookies": {
    "number": "1232456789"
  }
}
'''
# r = requests.get('https://www.12306.cn')

# print(r.status_code)

## Prepared Request
from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name':'germet'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/537.36 (KHTML,like Gecko) \
            Chrome/63.0.3239.132 Safari/537.36'
    } 

s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)

'''
运行结果：
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "germet"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)         AppleWebKit/537.36 (KHTML,like Gecko)             Chrome/63.0.3239.132 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65dc048d-5e69575d7fdeea8b0d6bf362"
  }, 
  "json": null, 
  "origin": "117.181.221.197", 
  "url": "http://httpbin.org/post"
}
'''
