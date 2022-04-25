
"""
@author OwarMag1c
@desc 电影排序模块
@date 2022/3/14
说明: 通过一定算法，对筛选tag交集后的电影计算其加权值，从而进行排序筛选
使用: 调用rank_films(film_infos, config)返回排序后的电影数据的List: films_after_rank，其结构如下:
films_after_rank: dict[name, film_weighted_value, film_web_list: List[website_score], 
                  film_dates, film_tags, film_areas, film_directors_and_actors, film_quote]
film_infos: List[tag_recommend_system_pb2.film_info]
config: config_parser.DataParser
"""

import os
import sys

now_path = os.getcwd()
conf_path = now_path + r"/../conf/"
util_path = now_path + r"/../util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()
import config_parser

def __get_film_reveal_info_weight(film_reveal_info):
  """获得film_reveal_info里的加权值"""
  return film_reveal_info['film_weighted_value']

def rank_films(film_infos: list, config: config_parser.DataParser):
  """通过一定算法，对筛选tag交集后的电影计算其加权值，从而进行排序筛选，返回筛选后的电影序列"""
  
  # 建立每部电影对应多个网站电影信息的字典
  film_info_dict = {}
  for film_info in film_infos:
    if film_info.film_id in film_info_dict:
      film_info_dict[film_info.film_id].append(film_info)
    else:
      film_info_dict[film_info.film_id] = [film_info]
  
  films_after_rank = []
  # 计算每部电影的加权值
  for film_info_key in film_info_dict:
    film_dates = -1
    film_tags = ''
    film_directors_and_actors = ''
    film_areas = ''
    film_quote = ''
    film_weighted_value = float(0) # 加权值
    film_web_list = [] # 所有网站得分
    for film in film_info_dict[film_info_key]:
      if(film.date != -1):
        film_dates = film.date
      if(film.tags != ''):
        film_tags = film.tags
      if(film.directors_and_actors != ''):
        film_directors_and_actors = film.directors_and_actors
      if(film.areas != ''):
        film_areas = film.areas
      if(film.quote != ''):
        film_quote = film.quote
      film_web_list.append(film.web_id + '得分:' + str(film.web_score) + '/' + str(film.web_full_score))
      website_weight = config.website_dict[film.web_id]['website_weight']
      film_weighted_value += float(website_weight) * float(film.web_score) / float(film.web_full_score)
    film_reveal_info = {'name': film_info_key, 'film_weighted_value': round(film_weighted_value, 2), 'film_web_list': film_web_list, 'film_dates': int(film_dates), 'film_tags': film_tags, 'film_areas': film_areas, 'film_directors_and_actors': film_directors_and_actors, 'film_quote': film_quote}
    films_after_rank.append(film_reveal_info)
  films_after_rank.sort(key=__get_film_reveal_info_weight, reverse=True)  # 根据film_weighted_value降序排序
  print(get_cur_info() + 'tag_films rank complete!')
  return films_after_rank
  