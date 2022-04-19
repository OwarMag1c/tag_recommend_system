"""
@author OwarMag1c
@desc 猫眼网站爬取解析模块
@date 2022/3/12
说明: 爬取猫眼特定页数据，并进行解析
使用: 主要接口crawl_maoyan(web_config)，返回爬取并解析后的电影数据
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
  "cookie": "__mta=146053771.1648882536977.1649234654077.1649234720469.62; uuid_n_v=v1; uuid=E49B7090B25111EC9B8EA77F9C585A6D40F527250A8F42F18E56B8980581297B; _csrf=40b24f4c591e43fe77e8df6f98cf09adfbb3f1c83c82e244135b82fac231e0b7; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1648882537; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=17fe90ed1c9c8-0ae6c7b3310497-9771a3f-384000-17fe90ed1c9c8; _lxsdk=E49B7090B25111EC9B8EA77F9C585A6D40F527250A8F42F18E56B8980581297B; __mta=146053771.1648882536977.1649232279277.1649232304612.41; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1649234720; _lxsdk_s=17ffe0bb0e4-d1a-cd8-e6e%7C%7C5"
}

def crawl_maoyan(web_config: list):
  """爬取猫眼电影content，并且解析，返回所有电影解析后的信息"""
  print(get_cur_info() + "crawl maoyan content!")
  url = web_config['url']
  print(url)
  film_list = []
  response = requests.get(url, headers=headers, timeout=10)
  soup = BeautifulSoup(response.text, 'lxml')
  # file = open('maoyan_info', 'w')
  # file.write(str(soup))
  # file.close()
  parse_maoyan(soup, film_list)
  return film_list

def parse_maoyan(soup, film_list: list):
  pass

