#!/usr/bin/python3
# author: seven
# 2023年10月12日

import requests

response = requests.get("https://www.baidu.com/")

# 返回CookieJar对象
cookiejar = response.cookies

# 将CookieJar转为字典


