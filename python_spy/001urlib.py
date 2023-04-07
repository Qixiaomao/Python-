from urllib import request,parse
import ssl


#response = urllib.request.urlopen("http://www.baidu.com")

#print(response.read().decode('utf-8'))

# 上边这个是用urllib.request方法

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

