
"""
@author OwarMag1c
@desc 请求消费服务端
@date 2022/3/17
说明: 服务器调用`python3 tag_recommend_system_server`
"""

from concurrent.futures import thread
import sys
import os
import time
import socket
import threading
import pickle

now_path = os.getcwd()
util_path = now_path + r"/util"
conf_path = now_path + r"/conf/"
proto_path = now_path + r"/proto/"
dao_path = now_path + r"/dao/"
crawler_path = now_path + r"/crawler/"
rank_path = now_path + r"/rank"
sys.path.append(rank_path)
sys.path.append(crawler_path)
sys.path.append(proto_path)
sys.path.append(conf_path)
sys.path.append(dao_path)
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
import crawler_core
import config_parser
import films_ranker
import tag_films_dao
import tag_recommend_system_pb2
import rsp_struct_creator

# 爬虫函数
def crawler_func(url_handle_manager):
  while(True):
    url_handle_manager.handle()
    time.sleep(3600)  # 爬虫间隔1小时

# 取交集处理
def intersection_request_handle(tag_list, tag_film_dao):
  film_name = set() # 去重集合
  for tag in tag_list:
    data_bin = tag_film_dao.get_value(tag)
    if data_bin == None:
      return ''
    tag_film_list = tag_recommend_system_pb2.tag_films()
    # tag_film_list = pickle.loads(data_bin)
    tag_film_list.ParseFromString(data_bin)
    if(len(film_name) == 0): # 第一个tag对应的电影名直接加入集合
      for film in tag_film_list.film_infos:
        film_name.add(film.film_id)
    else : # 否则加入其他集合，再与第一个tag的集合取交集
      tmp_film_name = set()
      for film in tag_film_list.film_infos:
        tmp_film_name.add(film.film_id)
      film_name = tmp_film_name & film_name
  return film_name

# 取并集处理
def union_request_handle(tag_list, tag_film_dao):
  film_name = set() # 去重集合
  for tag in tag_list:
    data_bin = tag_film_dao.get_value(tag)
    if data_bin == None:
      return ''
    tag_film_list = tag_recommend_system_pb2.tag_films()
    # tag_film_list = pickle.loads(data_bin)
    tag_film_list.ParseFromString(data_bin)
    if(len(film_name) == 0): # 第一个tag对应的电影名直接加入集合
      for film in tag_film_list.film_infos:
        film_name.add(film.film_id)
    else : # 否则加入其他集合，再与第一个tag的集合取交集
      tmp_film_name = set()
      for film in tag_film_list.film_infos:
        tmp_film_name.add(film.film_id)
      film_name = tmp_film_name | film_name
  return film_name

# 请求处理函数
def request_handle(data, config, tag_film_dao):
  # 拆分content和type
  request_type_and_content = data.split('&')
  if len(request_type_and_content) != 2:
    return ''
  
  # 拆分tag列表
  tag_list = request_type_and_content[0].split(',')
  if(len(tag_list) == 0):
    return ''
  
  films_result = []
  film_name = set() # 去重集合
  if (request_type_and_content[1] == 'intersection'):
    film_name = intersection_request_handle(tag_list, tag_film_dao)
  elif (request_type_and_content[1] == 'union'):
    film_name = union_request_handle(tag_list, tag_film_dao)
  
  # 对取集合里的所有数据
  data_bin = tag_film_dao.get_value(tag_list[0])
  if data_bin == None:
      return ''
  tag_film_list = tag_recommend_system_pb2.tag_films()
  tag_film_list.ParseFromString(data_bin)
  for film in tag_film_list.film_infos:
    if(film.film_id in film_name):
      films_result.append(film)
  
  # for tag in tag_list:
  #   data_bin = tag_film_dao.get_value(tag)
  #   if data_bin == None:
  #     return ''
  #   tag_film_list = tag_recommend_system_pb2.tag_films()
  #   # tag_film_list = pickle.loads(data_bin)
  #   tag_film_list.ParseFromString(data_bin)
  #   for film in tag_film_list.film_infos:
  #     if(film.film_id in film_name):
  #       continue
  #     films_result.append(film)
  #     film_name.add(film.film_id)
  films_result = films_ranker.rank_films(films_result, config)
  films_result = str(films_result[0 : 20])
  return films_result
    
# 线程函数
def tcp_link(sock, addr, config, tag_film_dao):
  print(get_cur_info() + ('Accept new connection from %s:%s' % (addr)))
  while(True):
    data = sock.recv(1024)
    if(not data):
      break
    print('receive data:' + data.decode())
    time.sleep(1)
    rsp = request_handle(data.decode(), config, tag_film_dao)
    rsp = str(rsp)
    rsp = str(len(rsp.encode())) + '@' + rsp
    # print(rsp)
    # file = open('rsp', 'a')
    # file.write(rsp + '\n')
    # file.close()
    r = sock.sendall(rsp.encode('utf-8'))
  sock.close()
  print(get_cur_info() + ('Connection from %s:%s closed!' % (addr)))
  
def main():
  config = config_parser.DataParser(now_path + "/conf/tag_recommend_system.yaml")
  tag_film_dao = tag_films_dao.TagFilmsDao()
  url_handle_manager = crawler_core.UrlHandleManager(config)
  crawler_thread = threading.Thread(target=crawler_func, args=(url_handle_manager,))
  crawler_thread.start()
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # 公网ip:175.27.135.19, port:9997
  s.bind(('0.0.0.0', 9997))
  s.listen(5)
  print(get_cur_info() + 'Waiting for connection...')
  while(True):
    sock, addr = s.accept()
    thread = threading.Thread(target=tcp_link, args=(sock, addr, config, tag_film_dao))
    thread.start()

if __name__ == '__main__':
  sys.exit(main())