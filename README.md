# Python-pyspider
存放自己爬虫项目

目的：爬取某网站发布的新冠信息

## 使用方式
covid_spider.py文件是实际爬取程序，spider里的两个文件夹内容是存储数据

## 代码逻辑简述
首先访问指定的网站，然后爬取网页内容，对爬取到的网页内容进行一个数据筛查，
提取需要的数据，保存到指定的json格式文件。

### 用到的库

``` python:

from encodings.utf_8 import encode
from pip import main
import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm

```


### 访问页面
```
 # 发送请求，获取疫情首页
        response = requests.get(url)
        return response.content.decode()
```


### 采集指定的数据
```
corona_virus = []
        for country in tqdm(last_day_covid,'采集近日以来各国的疫情数据'):  # tqdm为进度条显示
            # 发送请求，获取各国至今的json数据
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            #print(statistics_data_json_str)
            # 把json数据转换为python类型的数据，添加列表中
```

### 保存数据到文件

```
def save_data(self,path,data):
        # json格式保存
        with open(path,'w',encoding='utf8') as fp:
            json.dump(data,fp,ensure_ascii=False)
```

### 运行
