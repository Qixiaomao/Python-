#!/usr/bin/python3
# author: seven
# 2023年10月11日

#coding = utf-8

import requests
response = requests.get("http://www.sina.com")
print(response.request.headers)
print(response.content.decode())



