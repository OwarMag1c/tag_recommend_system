"""
@author OwarMag1c
@desc 烂番茄网站爬取解析模块
@date 2022/3/12
说明: 爬取烂番茄特定页数据，并进行解析
使用: 主要接口crawl_rotten_tomato(web_config)，返回爬取并解析后的电影数据
"""

from distutils.file_util import move_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
import time as ti

import sys
import os
now_path = os.getcwd()
util_path = now_path + r"/../util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()

ua = UserAgent()
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
}

def crawl_rotten_tomato(web_config: list):
  """爬取烂番茄的电影content，并且解析，返回所有电影解析后的信息"""
  print(get_cur_info() + "crawl rotten_tomato content!")
  url = web_config['url']
  print(url)
  film_list = []
  response = requests.get(url, headers=headers, timeout=10)
  soup = BeautifulSoup(response.text, 'lxml')
  # file = open('rotten_tomato_info', 'w')
  # file.write(str(soup))
  # file.close()
  parse_maoyan(soup, film_list)
  return film_list

def parse_maoyan(soup, film_list: list):
  pass

