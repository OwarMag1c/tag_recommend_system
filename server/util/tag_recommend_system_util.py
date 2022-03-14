
"""
@author OwarMag1c
@desc 通用模块
@date 2022/3/13
说明: 通用函数模块，集成所有通用函数
使用: 查看下列函数备注信息
"""

import sys
import os

def append_project_path():
  """添加项目子目录到系统变量"""
  now_path = os.getcwd()
  conf_path = now_path + r"/../conf/"
  proto_path = now_path + r"/../proto/"
  dao_path = now_path + r"/../dao/"
  crawler_path = now_path + r"/../crawler/"
  util_path = now_path + r"/../util/"
  rank_path = now_path + r"/../rank"
  sys.path.append(rank_path)
  sys.path.append(crawler_path)
  sys.path.append(proto_path)
  sys.path.append(conf_path)
  sys.path.append(dao_path)
  sys.path.append(util_path)

def get_cur_info():
  """返回调用方名与堆栈帧的帧对象，用于日志输出"""
  try:
    raise Exception
  except:
    f = sys.exc_info()[2].tb_frame.f_back
  return (str(f.f_code.co_filename) + ':' + str(f.f_code.co_name) + '[' + str(f.f_lineno) + ']' + ': ')
