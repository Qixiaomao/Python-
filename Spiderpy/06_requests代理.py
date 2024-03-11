#!/usr/bin/python3
# author: seven
# 2023年10月12日

import requests

# proxies
proxies = {
    "http":"http://89.29.100.210:3128",
    "https":"http://202.182.57.10:8080",
}

responsse = requests.get("https://www.baidu.com",proxies = proxies)
print(responsse.text)

# 准备IP池

{"ip":ip,"times":0}

