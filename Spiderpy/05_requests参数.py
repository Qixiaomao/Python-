#!/usr/bin/python3
# author: seven
# 2023年10月12日

import requests

formdata = {
    "type":"AUTO",
    "i":"i love you",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"ture"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=\
       rule&smartresult=ugc&sessionFrom=null"



headers = {"User-Agent":"Mozilla/5.0(Window NT 10.0; Win64; x64) \
        APPleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99\
            Safari/537.36"}

# 基本的GET请求可以直接用get方法
response = requests.get("https://www.baidu.com")

print(response)

# 基本的POST方法使用
response = requests.post(url,data=formdata, headers=headers)

print(response.text)  # response.text 是 str


