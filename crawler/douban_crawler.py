
"""
@author OwarMag1c
@desc 豆瓣网站爬取解析模块
@date 2022/3/12
说明: 爬取豆瓣特定页数据，并进行解析
使用: 主要接口crawl_douban(web_config)，返回爬取并解析后的电影数据
"""

from distutils.file_util import move_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

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
  'user-agent': ua.random,
  'Host': 'movie.douban.com',
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

def crawl_douban(web_config: list):
  """爬取豆瓣top250的电影content，并且解析，返回所有电影解析后的信息"""
  print(get_cur_info() + "crawl douban content!")
  url = web_config['url']
  film_list = []
  # 遍历top250的电影
  for index in range(0,10):
    next_url = url + "?start=" + str(index * 25)
    response = requests.get(next_url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, 'lxml')
    parse_duoban(soup, film_list)
  return film_list

def parse_duoban(soup, film_list: list):
  """解析豆瓣的content，结果加入movie_list"""
  div_list = soup.find_all('div', class_='info')
  for each in div_list:
    title = each.find('div', class_='hd').a.span.text.strip()
    each_str = str(each.find('div', class_='hd'))
    url_start_index = each_str.find('href=')
    url_end_index = each_str[:len(each_str)].find(r'/">')
    url = each_str[url_start_index + len(r'href="'):url_end_index + 1].strip()
    rating = each.find('span', class_='rating_num').text.strip()
    try:
        quote = each.find('span', class_='inq').text.strip()
    except:
        quote = ""
    info = each.find('div', class_='bd').p.text.strip()
    info = info.replace("\n", " ").replace("\xa0", " ")
    info = ' '.join(info.split())
    dates = ""
    for c in info:
      if(c.isdigit() == True):
        dates += c
    info_set = info.split(' ' + dates + ' / ')
    try:
      directors_and_actors = info_set[0]
      info_set = info_set[1].split(' / ')
      areas = info_set[0]
      tags = info_set[1].split(' ')
    except:
      directors_and_actors = ""
      areas = ""
      tags = ""
    film_info = {'title':title, 'rating': rating, 'dates': dates, 'tags': tags, 'areas': areas, 'directors_and_actors': directors_and_actors, 'quote': quote}
    
    # file = open('douban_info', 'a')
    # file.write(str(film_info) + '\n')
    # file.close()
    
    film_list.append(film_info)
