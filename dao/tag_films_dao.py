
"""
@author OwarMag1c
@desc DAO层Redis交互器
@date 2022/3/9
说明: DAO层，仅用于与Redis交接，包括存储、修改与获取数据
使用: 传入host和port初始化TagFilmsDao，即可调用实例化的成员函数与Redis交互
"""

from base64 import decode
from faulthandler import disable
from importlib.util import decode_source
from this import d
import redis
import sys
import os
now_path = os.getcwd()
util_path = now_path + r"/../util"
sys.path.append(util_path)
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path
append_project_path()

class TagFilmsDao:
  """Redis交接器"""
  def __init__ (self, host: str='localhost', port: int=6379):
    self.pool = redis.ConnectionPool(
      host=host, port=port, decode_responses=False)
    self.r = redis.Redis(connection_pool=self.pool)
    print(get_cur_info() + "pool init successfully!, host=%s, port=%d" % (host, port))

  def set_value(self, key: str, value: str or bytes, ex: int=-1):
    """如果不存在key则创建，否则修改，ex为过期时间，-1为默认为空, 设置成功返回True，否则False"""
    if(ex == -1):
      return self.r.set(key, value)
    else :
      return self.r.set(key, value, ex=ex)

  def set_new_value(self, key: str, value: str or bytes, ex: int=-1):
    """当key不存在时才执行新建，新建成功返回True，否则False"""
    if(ex == -1):
      return self.r.set(key, value, nx=True)
    else :
      return self.r.set(key,value, ex=ex, nx=True)
    
  def replace_value(self, key: str, value: str or bytes, ex=-1):
    """当key存在时才执行修改，修改成功返回True，否则False"""
    if(ex == -1):
      return self.r.set(key, value, xx=True)
    else :
      return self.r.set(key,value, ex=ex, xx=True)
     
  def set_value_batch(self, keys: list, values: list, exs: list):
    """批量设置值，keys、values、exs的数组大小必须相等,exs为空的位置需传入-1，全部设置成功返回True，否则False"""
    if((len(keys) != len(values)) or (len(keys) != len(exs))):
      return False
    for index in range(0, len(keys)):
      flag = self.set_value(keys[index], values[index], ex=exs[index])
      if(flag == False) :
        return False
    return True
  
  def get_value(self, key: str):
    """返回key对应的value"""
    return self.r.get(key)
  
  def get_value_batch(self, keys: list):
    """批量获取值，keys必须为list，返回值为values的list, 获取失败返回False"""
    if(type(keys) != list):
      return False
    return self.r.mget(keys)

