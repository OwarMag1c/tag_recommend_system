#！/usr/bin/env python

"""
@author OwarMag1c
@desc 配置读取解析器测试代码
@date 2022/3/10
"""

import config_parser
import sys
import os
now_path = os.getcwd()
util_path = now_path + r"/../util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()

def main():
  config = config_parser.DataParser('tag_recommend_system.yaml')
  print(get_cur_info(), config.website, config.crawler, config.redis)

if __name__ == '__main__':
  sys.exit(main())