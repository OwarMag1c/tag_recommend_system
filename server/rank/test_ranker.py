
import os
import sys
now_path = os.getcwd()
util_path = now_path + r"/../util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path

import films_ranker
import config_parser
import tag_recommend_system_pb2
import tag_films_dao

def main():
  config = config_parser.DataParser(now_path + "/../conf/tag_recommend_system.yaml")
  tag_film_dao = tag_films_dao.TagFilmsDao()
  data_bin = tag_film_dao.get_value('科幻')
  tag_film_list = tag_recommend_system_pb2.tag_films()
  tag_film_list.ParseFromString(data_bin)
  
  film_list = []
  # 打乱原本的顺序
  length = len(tag_film_list.film_infos)
  for film in range(int(length/2), length):
    film_list.append(tag_film_list.film_infos[film])
  for film in range(0, int(length/2)):
    film_list.append(tag_film_list.film_infos[film])
  
  films_after_rank = films_ranker.rank_films(film_list, config)
  
  file = open('films_after_rank', 'w')
  for film in films_after_rank:
    file.write(str(film) + '\n')
  file.close()

if __name__ == '__main__':
  sys.exit(main())