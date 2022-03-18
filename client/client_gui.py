#!/usr/bin/python
"""
@author OwarMag1c
@desc 客户端图形界面模块
@date 2022/3/17
说明: 展示图形界面
"""

import tkinter
import sys
import os

now_path = os.getcwd()
util_path = now_path + r"/../server/util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()


def main():
  if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
    
  #create main window
  master = tkinter.Tk()
  master.title("tester")
  master.geometry("300x100")


  #make a label for the window
  label1 = tkinter.Label(master, text='Hellooooo')
  # Lay out label
  label1.pack()

  # Run forever!
  master.mainloop()
  pass

if __name__ == '__main__':
  sys.exit(main())