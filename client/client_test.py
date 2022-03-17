#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9997))

print(s.recv(1024))

for data in ['zjw', 'ygl', 'lele']:
  s.send(data.encode())
  print(s.recv(1024))

while(True):
  data = 1