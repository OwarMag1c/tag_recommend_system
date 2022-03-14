
"""
@author OwarMag1c
@desc 数据更新模块
@date 2022/3/13
说明: 将最新数据pb结构化，并对数据库数据进行更新
使用: 主接口data_restore(film_list, web_id, config)，film_list:原始数据类型，web_id:网站名
"""

from distutils.command.config import config
import os
import sys

now_path = os.getcwd()
util_path = now_path + r"/../util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()

import config_parser
from tag_films_dao import TagFilmsDao
import film_struct_creator
import tag_recommend_system_pb2

def data_restore(film_list: list, web_id: 'str', config: config_parser.DataParser):
  """数据库更新新数据"""
  tag_films_dao = TagFilmsDao(host=config.redis['ip'], port=config.redis['port'])
  
  # 得到tag下的所有电影
  tag_film_dict = {}
  for film in film_list:
    for tag in film['tags']:
      if(tag in tag_film_dict):
        tag_film_dict[tag].append(film)
      else:
        tag_film_dict[tag] = [film]
  
  # 创造并存储数据
  for key in tag_film_dict:
    tag_films = tag_recommend_system_pb2.tag_films()
    tag_films_bin = tag_films_dao.get_value(key)        # 取tag的数据
    if(tag_films_bin != None):
      tag_films.ParseFromString(tag_films_bin)          # 反序列化
    films_set = set()                                   # 去重set
    for film in tag_films.film_infos:
      films_set.add(film.film_id + web_id)              # 当电影id和网站id都相同才进行去重
    for film in tag_film_dict[key]:                     # 写入新数据
      if((film['title'] + web_id) in films_set):
        continue
      film_info = film_struct_creator.create_film_info(film, web_id)
      tag_films.film_infos.append(film_info)
    new_tag_films_bin = tag_films.SerializeToString()   # 序列化
    tag_films_dao.set_value(key, new_tag_films_bin)     # 写回数据库
    
  print(get_cur_info() + 'data restore complete!')
      