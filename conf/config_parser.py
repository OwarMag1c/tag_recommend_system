
# 配置解析器，用于分发解析函数，存放结果字典
class DataParser:
  def __init__(self, data):
    self.data = data
    self.Parse()
    print('yaml_data parse complete!')
    
  # 解析分发
  def Parse(self):
    self.ParseWebsite(self.data)
    self.ParseDataBase(self.data)
    self.ParseCrawler(self.data)
      
  # 解析所有网站配置
  def ParseWebsite(self, data):
    self.website = data['website']
    
  # 解析redis配置
  def ParseDataBase(self, data):
    self.redis = data['redis']
  
  # 解析爬虫配置
  def ParseCrawler(self, data):
    self.crawler = data['crawler']