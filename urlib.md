# urlib库函数使用

## urlib库函数

* request:用来发起请求
* parse:用来解析域名地址，url目录
* error:处理异常
* robotparser:解析网站得robot.txt

这个函数是一个python内置得函数。
这个得参数有三个
`urllib.request.urlopen(url, data=None, [timeout, ]*)`，其中这个url是存放得请求连接，data用于post请求得时候，存放账号密码，timeout用于设置服务器得请求超时，如果超过时长，就不理他。

```python

import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")

print(response.read().decode('utf-8'))

```

需要导入得库
```
from urllib import request,parse
import ssl
```


`urllib.request.Request(url, data=None, headers={}, method=None)` 

使用案例：
```python:
context = ssl._create_unverified_context() #导入ssl证书

url = 'https://biihu.cc//account/ajax/login_process/'
headers = {
    #假装自己是浏览器
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

#请求参数
dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'xiaoshuaib@gmail.com',
    'password':'123456789',
    '_post_type':'ajax',
}
#定义参数
data = bytes(parse.urlencode(dict),'utf-8')

response = request.Request(url=url,data=data,headers=headers,method="POST")

response = request.urlopen(response,context=context)
print(response.read().decode('utf-8'))
```
