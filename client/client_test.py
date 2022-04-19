#!/usr/bin/python

import socket
import sys
import client_gui

def main():
  client_gui.gui_start()
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('175.27.135.19', 9997))

  print(s.recv(1024))

  for data in ['zjw', 'ygl', 'lele']:
    s.send(data.encode())
    print(s.recv(1024))

if __name__ == '__main__':
  sys.exit(main())