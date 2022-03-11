#！/usr/bin/env python

import yaml_reader
import data_parser
import sys

def main():
  yaml_data = yaml_reader.ReadYaml('tag_recommend_system.yaml')
  parser = data_parser.DataParser(yaml_data)
  print(parser.website, parser.crawler, parser.redis)

if __name__ == '__main__':
  sys.exit(main())