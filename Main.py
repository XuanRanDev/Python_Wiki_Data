import json
import re
import requests
import datetime
from bs4 import BeautifulSoup
import os

today = datetime.date.today().strftime("%Y%m%d")

def crawl_wiki_data():
    """
    爬取百度百科中青春由你2的参赛选手信息
    """
    heards = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    url = 'https://baike.baidu.com/item/青春有你第二季'

    try:
        response = requests.get(url, headers=heards)
        print(response.status_code)

        #  将数据传入BeautifulSoup中获得其对象
        soup = BeautifulSoup(response.text, 'lxml')

        # 返回是class为table-View
        tables = soup.find_all('div', {'data-index': '4_3'})

        return tables[0].find_next('table')


    except Exception as e:
        print(e)


def parseTable(table_data):
    """
    解析Table
    """

    bs = BeautifulSoup(str(table_data),'lxml')
    all_tr = bs.find_all('tr')

    error_list = ['\'', '\"']



if __name__ == '__main__':
    table_data = crawl_wiki_data()
    table_tr = parseTable(table_data)
