

import os
import sys
now_path = os.getcwd()
util_path = now_path + r"/../util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()

import data_updater
import config_parser

restore_list = []

file = open('film_info')
film_info = {}
index = 0
while True:
  line = file.readline()
  if(line):
    line = line[0: -1]
    if(index % 7 == 0):
      film_info = {}
      film_info['title'] = line
    if(index % 7 == 1):
      film_info['rating'] = line
    if(index % 7 == 2):
      film_info['dates'] = line
    if(index % 7 == 3):
      tags = line.split(' / ')
      film_info['tags'] = tags
    if(index % 7 == 4):
      film_info['areas'] = line
    if(index % 7 == 5):
      film_info['directors_and_actors'] = line
    if(index % 7 == 6):
      film_info['quote'] = line
      restore_list.append(film_info)
  else: 
    break
  index += 1

config = config_parser.DataParser(now_path + "/../conf/tag_recommend_system.yaml")
print(restore_list)
data_updater.data_restore(restore_list, config.website_dict['douban']['name'], config)

file.close()
