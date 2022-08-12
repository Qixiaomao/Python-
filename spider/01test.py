# 导入模块

import requests

# 发出请求响应
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')

# 获取数据
print(response.content.decode())