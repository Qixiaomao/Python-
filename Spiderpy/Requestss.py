# 爬虫模板
import requests

# 连接
get_url = 'https://www.xxxx.com'

# 构造请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# 写入载荷
params = {'key':'value'}
data = {'username':'user','passowrd':'password'}


# 请求连接
request_get = requests.get(get_url,params=params,data=data) # 使用了get方法
request_post = requests.post(get_url,params=params,data=data) # 使用了post方法

