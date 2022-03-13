#！/usr/bin/env python

"""
@author OwarMag1c
@desc 爬虫调度分发器测试代码
@date 2022/3/13
"""

import crawler_core
import sys

def main():
  url_handle_manager = crawler_core.UrlHandleManager()
  url_handle_manager.handle()

if __name__ == '__main__':
  sys.exit(main())