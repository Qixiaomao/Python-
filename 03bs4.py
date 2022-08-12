# 提取新冠网页的数据并进行简单的解析
import requests
from bs4 import BeautifulSoup
import re
import json

# 页面请求
web_page = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')

# 拿到页面信息
text = web_page.content.decode()

# 利用bs4进行解析
soup = BeautifulSoup(text,'lxml')

# 提取指定的标签
s = soup.find(id = 'getListByCountryTypeService2true')
text1 = s.text

# 提取json字符串
json_str = re.findall(r'(\[.*\])',text1)[0]
# print(json_str)

# json字符串转换为python类型的数据
last_day_corona_virus = json.loads(json_str)
print(last_day_corona_virus)