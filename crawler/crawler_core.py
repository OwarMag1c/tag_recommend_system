
from email import contentmanager
from flask import request
import requests
import os
import sys
import douban_crawler

now_path = os.getcwd()
conf_path = now_path + r"/../conf/"
proto_path = now_path + r"/../proto/"
dao_path = now_path + r"/../dao/"
sys.path.append(proto_path)
sys.path.append(conf_path)
sys.path.append(dao_path)

import tag_recommend_system_pb2
import data_restorer
from tag_films_dao import TagFilmsDao
import film_struct_creator
import yaml_reader
import config_parser

# 采用策略设计模式，对在配置中开关开启的url进行分发解析
class UrlHandleManager:
  def __init__(self):
    data = yaml_reader.ReadYaml(conf_path + 'tag_recommend_system.yaml')
    self.config = config_parser.DataParser(data)
    print('UrlHandleManager init complete!')
    
  # 对已在配置中注册的网站进行遍历
  def Handle(self):
    for web_config in self.config.website:
      if(web_config['switch'] == 1):
        self.Dispatch(web_config)
      
  # 对需要爬取网站content进行分发解析与数据存储
  def Dispatch(self, web_config):
    movie_list = []
    if(web_config['name'] == 'douban'):
      movie_list =  douban_crawler.CrawlDouban(web_config)
    elif(web_config['name'] == 'zhihu'):
      pass
    else:
      pass
    # 数据结构化与存储
    data_restorer.data_restore(movie_list, web_config['name'])
    