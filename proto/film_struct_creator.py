
import tag_recommend_system_pb2

# 根据电影信息列表创建并返回pb协议结构体tag_films
def CreateTagFilmsPb(film_lists, web_id):
  tag_films_ = tag_recommend_system_pb2.tag_films()
  for film in film_lists:
    film_info = CreateFilmInfoPb(film, web_id)
  return tag_films_
  
# 根据单条电影信息创建并返回pb协议结构体film_info
def CreateFilmInfoPb(film, web_id):
  film_info_ = tag_recommend_system_pb2.film_info()
  film_info_.film_id = film['title']
  film_info_.web_id = web_id
  film_info_.web_score = float(film['rating'])
  if(web_id == 'douban'):
    film_info_.web_full_score = float(10)
  else:
    film_info_.web_full_score = float(100)
  film_info_.dates = int(film['dates'])
  for tag in film['tags']:
    film_info_.tags.append(tag)
  film_info_.areas = film['areas']
  film_info_.directors_and_actors = film['directors_and_actors']
  film_info_.quote = film['quote']
  return film_info_