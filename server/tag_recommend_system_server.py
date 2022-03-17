
"""
@author OwarMag1c
@desc 请求消费服务端
@date 2022/3/17
说明: 消费客户端的请求
使用: 
"""

from concurrent.futures import thread
import sys
import os
import time
import socket
import threading

now_path = os.getcwd()
util_path = now_path + r"/util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()

# 线程函数
def tcp_link(sock, addr):
  print(get_cur_info() + ('Accept new connection from %s:%s' % (addr)))
  sock.send(('welcome!').encode())
  while(True):
    data = sock.recv(1024)
    time.sleep(1)
    if(data == 'exit' or not data):
      break
    sock.send(('hello, %s' % (data)).encode())
  sock.close()
  print(get_cur_info() + ('Connection from %s:%s closed!' % (addr)))
  
def main():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('127.0.0.1', 9997))
  s.listen(5)
  print(get_cur_info() + 'Waiting for connection...')
  while(True):
    sock, addr = s.accept()
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()
  pass

if __name__ == '__main__':
  sys.exit(main())