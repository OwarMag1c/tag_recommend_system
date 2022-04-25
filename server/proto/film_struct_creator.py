
"""
@author OwarMag1c
@desc pb结构化模块
@date 2022/3/12
说明: 将原始数据类型转换成pb结构体
使用: create_tag_films(film_lists, web_id): 生成tag_films；create_film_info(film, web_id): 生成film_info；
"""

import tag_recommend_system_pb2

def create_tag_films(film_lists: list, web_id: str):
  """根据film_lists与web_id生成tag_films"""
  tag_films = tag_recommend_system_pb2.tag_films()
  for film in film_lists:
    film_info = create_film_info(film, web_id)
    tag_films.film_infos.append(film_info)
  return tag_films
  
def create_film_info(film: dict, web_id: str):
  """根据film与web_id生成film_info"""
  film_info_ = tag_recommend_system_pb2.film_info()
  film_info_.film_id = film['title']
  film_info_.web_id = web_id
  film_info_.web_score = float(film['rating'])
  if(web_id == 'douban'):
    film_info_.web_full_score = float(10)
  else:
    film_info_.web_full_score = float(100)
  film_info_.date = int(film['dates'])
  for tag in film['tags']:
    film_info_.tags.append(tag)
  film_info_.areas = film['areas']
  film_info_.directors_and_actors = film['directors_and_actors']
  film_info_.quote = film['quote']
  return film_info_