import yaml

# 读取yaml，返回读到的数据
def read_yaml(file_name, encoding='utf-8'):
  file = open(file_name, 'r', encoding=encoding)
  file_data = file.read()
  file.close()
  return yaml.load(file_data, Loader=yaml.FullLoader)