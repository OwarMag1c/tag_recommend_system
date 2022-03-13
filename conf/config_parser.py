"""
@author OwarMag1c
@desc 配置读取解析器
@date 2022/3/10
说明: yaml配置解析
使用: 传入配置文件路径初始化DataParser，解析结果直接使用成员变量即可
"""

from typing import Dict
import yaml
import sys
import os
now_path = os.getcwd()
util_path = now_path + r"/../util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()

class DataParser:
  """配置解析器，用于分发解析函数，存放结果字典"""
  def __init__(self, file_name: str, encoding: str='utf-8'):
    self.__data = self.read_yaml(file_name, encoding)
    self.__parse()
    print(get_cur_info() + 'yaml_data parse complete!')

  def __parse(self):
    """解析分发"""
    self.__parse_website(self.__data)
    self.__parse_data_base(self.__data)
    self.__parse_crawler(self.__data)
      
  def __parse_website(self, data: dict):
    """解析所有网站配置"""
    self.website = data['website']
    
  def __parse_data_base(self, data: dict):
    """解析redis配置"""
    self.redis = data['redis']
  
  def __parse_crawler(self, data: dict):
    """解析爬虫配置"""
    self.crawler = data['crawler']

  def read_yaml(self, file_name: str, encoding: str='utf-8'):
    """读取yaml，返回读到的数据"""
    file = open(file_name, 'r', encoding=encoding)
    file_data = file.read()
    file.close()
    return yaml.load(file_data, Loader=yaml.FullLoader)