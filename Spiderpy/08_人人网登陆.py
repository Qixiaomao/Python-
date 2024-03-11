#!/usr/bin/python3
# author: seven
# 2023年10月12日

import  requests

headers = {"User-Agent":"Mozilla/5.0(Window NT 10.0; Win64; x64) \
        APPleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99\
            Safari/537.36"}

session = requests.session()
post_url = "http://www.renren.com/Plogin.do"
post_data = {"email":"18948796072","password":"lizhilong123"}

# 使用session 发送post请求，cookie 保存其中
session.post(post_url,data=post_data,headers=headers)

# 使用session 进行请求登陆之后才能访问的地址
r = session.get("http://www.renren.com/63012180/profile",headers = headers)

with open("renren.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())

