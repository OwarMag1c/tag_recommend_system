#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author OwarMag1c
@desc 客户端图形界面模块
@date 2022/3/17
说明: 展示图形界面
"""
from cgi import test
from ipaddress import collapse_addresses
from logging import root
import socket
from sqlite3 import Cursor
from this import s
from tkinter import *
import hashlib
import time
from tkinter.tix import COLUMN
from turtle import window_height, window_width

LOG_LINE_NUM = 0

class tag_films_recommend_gui():
  def __init__(self, init_window_name):
    self.init_window = init_window_name
    self.tag_state = [False] * 50
    self.output_text = [StringVar()] * 10
    self.time_text = StringVar()
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect(('175.27.135.19', 9997))
    self.tag_map = {0:'恐怖', 1:'剧情', 2:'爱情', 3:'同性', 4:'动画', 5:'奇幻', 6:'战争', 7:'历史', 8:'科幻', 9:'悬疑', 10:'冒险',
      11:'音乐', 12:'喜剧', 13:'歌舞', 14:'传记', 15:'家庭', 16:'运动', 17:'惊悚', 18:'武侠', 19:'古装', 20:'儿童', 21:'灾难',
      22:'犯罪', 23:'纪录片'
    }

  # 计算窗口居中坐标
  def center_window(self, master, width, height):
    ws = master.winfo_screenwidth()
    hs = master.winfo_screenheight()
    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)
    return (x, y)

  # 标签选择命令
  def rb_command(self, tag_index):
    if(self.tag_state[tag_index]):
      self.tag_state[tag_index] = False
    else:
      self.tag_state[tag_index] = True

  # 设置标签图形
  def set_tag(self, text, command, row, column):
    self.rb = Checkbutton(self.tag_frame, text=text, command=command, relief=RAISED, height=2, width=5, bd=5, cursor='circle', font=('幼圆', 13), bg='pink')
    self.rb.grid(row=row, column=column, padx=20, pady=10)

  # 设置窗口
  def set_init_window(self):
    self.init_window.title("优质电影推荐_v0.1")           # 窗口名
    
    self.window_width = 1480
    self.window_height = 850 
    coordinate = self.center_window(self.init_window, self.window_width, self.window_height)
    self.init_window.geometry('%dx%d+%d+%d' % (self.window_width, self.window_height, coordinate[0], coordinate[1]))
    self.init_window.resizable(False, False)
    self.init_window['bg'] = 'pink'                                    # 窗口背景色

    # 标签
    self.title_label = Label(self.init_window, text='电  影  推  荐  系  统', bg='pink', bd=5, font=('幼圆', 35), justify=CENTER, padx=100)
    self.title_label.grid(row=0, column=2)

    self.tag_title_label = Label(self.init_window, text='TAG选择', bg='pink', bd=5, font=('幼圆', 25), justify=CENTER)
    self.tag_title_label.grid(row=1, column=2 ,padx=10)

    # TAG选择框
    self.tag_frame = Frame(width=600, height=700,bg='pink')
    self.tag_frame.grid(row=2, column=2)
    self.set_tag('恐怖', lambda: self.rb_command(0), 3, 4)
    self.set_tag('剧情', lambda: self.rb_command(1), 3, 6)
    self.set_tag('爱情', lambda: self.rb_command(2), 3, 8)
    self.set_tag('同性', lambda: self.rb_command(3), 4, 4)
    self.set_tag('动画', lambda: self.rb_command(4), 4, 6)
    self.set_tag('奇幻', lambda: self.rb_command(5), 4, 8)
    self.set_tag('战争', lambda: self.rb_command(6), 5, 4)
    self.set_tag('历史', lambda: self.rb_command(7), 5, 6)
    self.set_tag('科幻', lambda: self.rb_command(8), 5, 8)
    self.set_tag('悬疑', lambda: self.rb_command(9), 6, 4)
    self.set_tag('冒险', lambda: self.rb_command(10), 6, 6)
    self.set_tag('音乐', lambda: self.rb_command(11), 6, 8)
    self.set_tag('喜剧', lambda: self.rb_command(12), 7, 4)
    self.set_tag('歌舞', lambda: self.rb_command(13), 7, 6)
    self.set_tag('传记', lambda: self.rb_command(14), 7, 8)
    self.set_tag('家庭', lambda: self.rb_command(15), 8, 4)
    self.set_tag('运动', lambda: self.rb_command(16), 8, 6)
    self.set_tag('惊悚', lambda: self.rb_command(17), 8, 8)
    self.set_tag('武侠', lambda: self.rb_command(18), 9, 4)
    self.set_tag('古装', lambda: self.rb_command(19), 9, 6)
    self.set_tag('儿童', lambda: self.rb_command(20), 9, 8)
    self.set_tag('灾难', lambda: self.rb_command(21), 10, 4)
    self.set_tag('犯罪', lambda: self.rb_command(22), 10, 6)
    self.set_tag('纪录片', lambda: self.rb_command(23), 10, 8)

    self.tag_select_button = Button(self.tag_frame, text='点击推荐!', bg='pink', bd=5, font=('幼圆', 25), justify=CENTER, cursor='circle', command=self.tag_select_button_command)
    self.tag_select_button.grid(row=24, column=6, pady=20, padx=20)
    
    self.response_frame = Frame(width=670, height=670, bg='pink')
    self.response_frame.grid(row=2, column=3)
    self.output_time_label = Label(self.response_frame, bg='pink', textvariable=self.time_text, bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_time_label.grid(row=0, column=0)
    self.output_label = Label(self.response_frame, bg='pink', textvariable=self.output_text[0], bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_label.grid(row=4, column=0)
    self.output_label = Label(self.response_frame, bg='pink', textvariable=self.output_text[0], bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_label.grid(row=5, column=0)
    self.output_label = Label(self.response_frame, bg='pink', textvariable=self.output_text[0], bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_label.grid(row=6, column=0)
    self.output_label = Label(self.response_frame, bg='pink', textvariable=self.output_text[0], bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_label.grid(row=7, column=0)
    self.output_label = Label(self.response_frame, bg='pink', textvariable=self.output_text[0], bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_label.grid(row=8, column=0)
    self.output_label = Label(self.response_frame, bg='pink', textvariable=self.output_text[0], bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_label.grid(row=9, column=0)
    self.output_label = Label(self.response_frame, bg='pink', textvariable=self.output_text[0], bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_label.grid(row=10, column=0)
    self.output_label = Label(self.response_frame, bg='pink', textvariable=self.output_text[0], bd=5, font=('幼圆', 15), justify=LEFT, anchor='sw')
    self.output_label.grid(row=11, column=0)
    
  # 构造并发送请求
  def tag_select_button_command(self):
    self.time_text.set('当前时间：' + self.get_current_time())
    tag_list_req = ''
    flag = 0
    for index in range(24):
      if(self.tag_state[index]):
        if(flag == 1):
          tag_list_req += ','
        tag_list_req += self.tag_map[index]
        flag = 1
    print(tag_list_req)

    self.socket.send(tag_list_req.encode())
    rsp = self.socket.recv(1024)
    print(rsp.decode())

  # 获取当 前时间
  def get_current_time(self):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time

def gui_start():
  init_window = Tk()              # 实例化出一个父窗口
  ZMJ_PORTAL = tag_films_recommend_gui(init_window)
  # 设置根窗口默认属性
  ZMJ_PORTAL.set_init_window()

  init_window.mainloop()          # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示