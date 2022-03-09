#！/usr/bin/env python

import sys
from tag_films_dao import TagFilmsDao

def main():
  tag_films_dao = TagFilmsDao(host='localhost', port=6379)
  
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