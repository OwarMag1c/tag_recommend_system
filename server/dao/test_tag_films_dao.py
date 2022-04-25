#！/usr/bin/env python

"""
@author OwarMag1c
@desc Redis交接器测试代码
@date 2022/3/9
"""

from asyncore import read
from audioop import add
import os
import sys

from tag_films_dao import TagFilmsDao

now_path = os.getcwd()
add_path = now_path + r"/../conf/"
sys.path.append(add_path)
print("%s add_path has been added!" % (add_path))

import config_parser

def main():
  config = config_parser.DataParser(os.getcwd() + r"/../conf/tag_recommend_system.yaml")
  
  tag_films_dao = TagFilmsDao(host=config.redis['ip'], port=config.redis['port'])
  
  print('set_new_value return=' + str(tag_films_dao.set_new_value('test_set_key', 'test_set_value_1')))
  keys = ['t_k_1', 't_k_2']
  values = ['t_v_1', 't_v_2']
  exs = [-1, -1]
  print('set_value_batch return=' + str(tag_films_dao.set_value_batch(keys, values, exs)))
  
  print(tag_films_dao.get_value('test_set_key'))
  print(tag_films_dao.get_value('no_key'))
  print(tag_films_dao.get_value_batch(['t_k_1', 't_k_2']))

if __name__ == '__main__':
  sys.exit(main())