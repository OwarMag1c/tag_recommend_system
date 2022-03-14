#！/usr/bin/env python

"""
@author OwarMag1c
@desc 爬虫调度分发器测试代码
@date 2022/3/13
"""

import crawler_core
import sys
import os

now_path = os.getcwd()
conf_path = now_path + r"/../conf/"
util_path = now_path + r"/../util"
sys.path.append(util_path)

import config_parser

def main():
  config = config_parser.DataParser(now_path + "/../conf/tag_recommend_system.yaml")
  url_handle_manager = crawler_core.UrlHandleManager(config)
  url_handle_manager.handle()

if __name__ == '__main__':
  sys.exit(main())