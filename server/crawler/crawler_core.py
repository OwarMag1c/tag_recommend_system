
"""
@author OwarMag1c
@desc 爬虫调度分发器
@date 2022/3/12
说明: 采用策略设计模式，遍历在配置中开启开关的网站分发调度爬虫，解析并对数据库更新数据
使用: 初始化UrlHandleManager(config)后调用成员函数handle()
"""

from distutils.command.config import config
import os
import sys
import douban_crawler
import maoyan_crawler
import rotten_tomato_crawler

now_path = os.getcwd()
util_path = now_path + r"/../util"
sys.path.append(util_path)

from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()

import data_updater
import config_parser

class UrlHandleManager:
  """采用策略设计模式，对在配置中开关开启的网站进行分发调度爬虫"""
  def __init__(self, config: config_parser.DataParser):
    self.__config = config
    print(get_cur_info() + 'UrlHandleManager init complete!')
    
  def handle(self):
    """对已在配置中注册的网站进行遍历调度"""
    for web_config in self.__config.website:
      if(web_config['switch'] == 1):
        self.__dispatch(web_config)
      
  def __dispatch(self, web_config: list):
    """对数据进行分发解析与存储"""
    movie_list = []
    if(web_config['name'] == 'douban'):
      movie_list = douban_crawler.crawl_douban(web_config)
    elif(web_config['name'] == 'maoyan'):
      maoyan_crawler.crawl_maoyan(web_config)
    elif(web_config['name'] == 'rotten_tomato'):
      rotten_tomato_crawler.crawl_rotten_tomato(web_config)
    else:
      pass
    # 数据结构化与存储
    data_updater.data_restore(movie_list, web_config['name'], self.__config)
    