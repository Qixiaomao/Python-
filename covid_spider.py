from encodings.utf_8 import encode
from pip import main
import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm

'''爬虫类'''

class covid_spider(object):
    
    '''初始化'''
    def __init__(self) -> None:
        self.webpage_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    
    def get_content_from_url(self,url):
        '''根据URL，获取响应内容的字符串数据
        param url:请求的url
        return:响应内容的字符串
        '''
        # 发送请求，获取疫情首页
        response = requests.get(url)
        return response.content.decode()
       
    def parse_home_page(self,home_page,tag_id):
        '''
        解析首页内容，获取解析后的python数据
        ''' 
       

        # 疫情首页，获取最近一日各国疫情数据
        soup = BeautifulSoup(home_page,'lxml')
        script = soup.find(id=tag_id)
        t = script.text

        # 从疫情数据中，获取json的数据
        json_str = re.findall(r'(\[.*\])',t)[0]



        # json -> python数据类型
        data = json.loads(json_str)
        return data
    
    def crawl_covid(self):
        '''采集最近一天的各国疫情信息'''
        with open('E:/local_post/python_example/alrog/tk/spider/data/last_covid_data.json','r',encoding='gb18030',errors='ignore') as fp:
            last_day_covid = json.load(fp)
        # print(last_day_covid)
        # 遍历各国疫情，获取统计的URL
        # 定义列表，用于存储各国1月23日以来的疫情数据
        corona_virus = []
        for country in tqdm(last_day_covid,'采集近日以来各国的疫情数据'):  # tqdm为进度条显示
            # 发送请求，获取各国至今的json数据
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            #print(statistics_data_json_str)
            # 把json数据转换为python类型的数据，添加列表中
            statistics_data = json.loads(statistics_data_json_str)
            print(type(statistics_data))
            #print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                one_day['countryShortCode'] = country['countryShortCode']
            # print(statistics_data)
            corona_virus.extend(statistics_data)
            # 保存数据
            self.save_data(corona_virus,'E:/local_post/python_example/alrog/tk/spider/data/last_covid_data.json')
      
    def crawl_covid_of_china(self):
        home_page = self.get_content_from_url(self.webpage_url)
        # 疫情首页，获取最近一日各国疫情数据
        
        '''
        代码复用
        soup = BeautifulSoup(home_page,'lxml')
        script = soup.find(id='getAreaStat')
        t = script.text
        # 从疫情数据中，获取json的数据
        json_str = re.findall(r'(\[.*\])',t)[0]
        # json -> python数据类型
        data = json.loads(json_str)
        # 保存疫情数据
        self.save_data('alrog/tk/spider/data/last_covid_china.json',data)   
        '''
        last_covid_china = self.parse_home_page(home_page,tag_id='getAreaStat')
        self.save_data('alrog/tk/spider/data/last_covid_china.json',last_covid_china)
        
    def crawl_covid_of_china(self):
        # 加载最近一日全国疫情信息，获取各省疫情URL
        with open('alrog/tk/spider/data/last_covid_china.json','r',encoding='utf8',errors='ignore') as fp:
            last_covid_china = json.load(fp)
            
            covid_china = []
            
            for province in tqdm(last_covid_china,'采集各个省市的疫情情况'):
                statics_data_url = province['statisticsData']
                statics_data_json_str = self.get_content_from_url(statics_data_url)
                statistics_data = json.loads(statics_data_json_str)['data']
                
                for one_day in statistics_data:
                    one_day['provinceName'] = province['provinceName']
                    
                covid_china.extend(statistics_data)
                # print(covid_china)
            #  保存到指定的文件
            self.save_data('alrog/tk/spider/data/last_covid_of_china.json',covid_china)
             
    def save_data(self,path,data):
        # json格式保存
        with open(path,'w',encoding='utf8') as fp:
            json.dump(data,fp,ensure_ascii=False)
            
    def crawl_last_day_corona_virus(self):
        '''
        采集一天的各国疫情信息
        '''
        # 发送请求
        home_page = self.get_content_from_url(self.webpage_url)
        # 解析网页内容
        last_day_covid_data = self.parse_home_page(home_page,tag_id='getListByCountryTypeService2true')
        # 保存数据
        self.save_data('alrog/tk/spider/data/last_covid_data.json',last_day_covid_data)
        
    def run(self):
        # self.crawl_last_day_corona_virus()
        # self.crawl_covid_of_china()
        self.crawl_covid_of_china()
        
if __name__ == '__main__':
    spi = covid_spider()
    spi.run()