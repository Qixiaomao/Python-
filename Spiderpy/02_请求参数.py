#!/usr/bin/python3
# author: seven
# 2023年10月11日

import  requests

#  字典
kyw = {'wd':'长城'}

headers = {"User-Agent":"Mozilla/5.0(Window NT 10.0; Win64; x64) \
        APPleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99\
            Safari/537.36"}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response  = requests.get("http://www.baidu.com/s?", params = kyw, headers = headers)

# 查看相应内容，response.text 返回的Unicode 格式的数据

# 我们可以把text的内容拿到dw中去看
print(response.text)

# 查看响应内容，response.content 返回的字节流数据
print(response.content)

# 查看完整的url地址
print(response.url)

# 查看相应头部字符编码
print(response.encoding)

# 查看响应码
print(response.status_code)

# 查看响应头
print(response.headers)

print(response.request.headers)

