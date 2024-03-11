import re
import requests
import json
import time
from requests.exceptions import RequestException


# 获取首页
def get_one_page(urls):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/537.36 (KHTML,like Gecko) \
            Chrome/63.0.3239.132 Safari/537.36'
    }
    
    r = requests.get(url=urls,headers=headers)
    if r.status_code == 200:
        return r.text
 
# 解析页面
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>\
        (.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>\
            (.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )   
    items = re.findall(pattern,html)
    # 遍历结果并提取结果
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip() + item[6].strip()
        }
        
# 写入文件
def write_to_file(content):
    try:
        with open('test1.txt','a',encoding='utf-8') as f:
        # print(type(json.dumps(content)))
            f.write(json.dumps(content,ensure_ascii=False)+'\n')
            print('Write successful!\n')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        

def main(offset):
    # 目标
    urls = 'https://www.maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(urls)
    for item in parse_one_page(html):
        write_to_file(item)
    
if __name__ == '__main__':
    for i in range(10):
       main(offset=i*10)
       time.sleep(1)
    print('load successful!\n')
