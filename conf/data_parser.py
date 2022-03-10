
# 数据解析器，用于分发解析函数，存放结果字典
class data_parser:
  def __init__(self, data):
    self.data = data
    self.parse()
    print('yaml_data parse complete!')
    
  # 解析分发
  def parse(self):
    self.parse_website(self.data)
    self.parse_data_base(self.data)
    self.parse_crawler(self.data)
      
  # 解析所有网站配置
  def parse_website(self, data):
    self.douban = data['douban']
    
  # 解析redis配置
  def parse_data_base(self, data):
    self.redis = data['redis']
  
  # 解析爬虫配置
  def parse_crawler(self, data):
    self.crawler = data['crawler']