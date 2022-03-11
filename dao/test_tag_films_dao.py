#！/usr/bin/env python

from asyncore import read
from audioop import add
import os
import sys

from tag_films_dao import TagFilmsDao

now_path = os.getcwd()
add_path = now_path + r"/../conf/"
sys.path.append(add_path)
print("%s add_path has been added!" % (add_path))

import data_parser
import yaml_reader

def main():
  
  data = yaml_reader.ReadYaml(os.getcwd() + r"/../conf/tag_recommend_system.yaml")
  config = data_parser.DataParser(data)
  print("data parse over!", config.douban, config.redis, config.crawler)
  
  tag_films_dao = TagFilmsDao(host=config.redis['ip'], port=config.redis['port'])
  
  print('SetNewValue return=' + str(tag_films_dao.SetNewValue('test1', 'test_value_1')))
  print('SetValue return=' + str(tag_films_dao.SetValue('test2', 'test_v_2')))
  keys = ['tb1', 'tb2']
  values = ['tb_v_1', 'tb_v_2']
  exs = [-1, -1]
  print('SetValueBatch return=' + str(tag_films_dao.SetValueBatch(keys, values, exs)))
  
  print(tag_films_dao.GetValue('test1'))
  print(tag_films_dao.GetValue('test2'))
  print(tag_films_dao.GetValueBatch(['tb1', 'tb2']))

if __name__ == '__main__':
  sys.exit(main())