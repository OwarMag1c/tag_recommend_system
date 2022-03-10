#！/usr/bin/env python

import yaml_reader
import data_parser
import sys

def main():
  yaml_data = yaml_reader.read_yaml('tag_recommend_system.yaml')
  parser = data_parser.data_parser(yaml_data)
  print(parser.douban, parser.crawler, parser.redis)

if __name__ == '__main__':
  sys.exit(main())