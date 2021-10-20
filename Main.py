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