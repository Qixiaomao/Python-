#!/usr/bin/python3
# author: seven
# 2023年10月11日
# 通过requests获取网络上的图片大小

from io import BytesIO, StringIO
import requests
from PIL import Image

img_url = "https://baidu.com/img/bd_logo1.png"
response = requests.get(img_url)

f = BytesIO(response.content)
img = Image.open(f)
print(img.size)




# 数据读写不一定是文件，也可以在内存中读写
# StringIO 意思就是在内存中读写str
# BytesIO 就是在内存中读写bytes类型的二进制数据