
import os
import sys

now_path = os.getcwd()
conf_path = now_path + r"/../conf/"
dao_path = now_path + r"/../dao/"
sys.path.append(conf_path)
sys.path.append(dao_path)

import yaml_reader
import config_parser
from tag_films_dao import TagFilmsDao
import film_struct_creator
import tag_recommend_system_pb2

# 数据库插入新数据
def data_restore(film_list, web_id) :
  data = yaml_reader.ReadYaml(os.getcwd() + r"/../conf/tag_recommend_system.yaml")
  config = config_parser.DataParser(data)
  tag_films_dao = TagFilmsDao(host=config.redis['ip'], port=config.redis['port'])
  
  # 得到tag下的所有电影
  tag_film_dict = {}
  for film in film_list:
    for tag in film['tags']:
      if(tag in tag_film_dict):
        tag_film_dict[tag].append(film)
      else:
        tag_film_dict[tag] = []
  
  # 创造并存储数据
  for key in tag_film_dict:
    tag_films = tag_recommend_system_pb2.tag_films()
    tag_films_bin = tag_films_dao.GetValue(key)         # 取tag的数据
    if(tag_films_bin != None):
      tag_films.ParseFromString(tag_films_bin)          # 反序列化
    films_set = set()                                   # 去重set
    for film in tag_films.film_infos:
      films_set.add(film.film_id)
    for film in tag_film_dict[key]:                     # 写入新数据
      if(film['title'] in films_set):
        continue
      film_info = film_struct_creator.CreateFilmInfoPb(film, web_id)
      tag_films.film_infos.append(film_info)
    new_tag_films_bin = tag_films.SerializeToString()   # 序列化
    tag_films_dao.SetValue(key, new_tag_films_bin)      # 写回数据库
    
  print('data restore complete!')
      