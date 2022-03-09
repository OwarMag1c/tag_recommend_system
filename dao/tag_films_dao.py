#！/usr/bin/env python

from base64 import decode
from importlib.util import decode_source
from this import d
import redis

class TagFilmsDao:
  # Redis交接层
  def __init__ (self, host='localhost', port=6379):
    self.pool = redis.ConnectionPool(
      host=host, port=port, decode_responses=True)
    self.r = redis.Redis(connection_pool=self.pool)
    print("pool init successfully!, host=%s, port=%d" % (host, port))

  # 如果不存在key则创建，否则修改，ex为过期时间，-1为默认为空
  # 设置成功返回True，否则False
  def SetValue(self, key, value, ex=-1):
    if(ex == -1):
      return self.r.set(key, value)
    else :
      return self.r.set(key, value, ex=ex)

  # 当key不存在时才执行新建
  # 新建成功返回True，否则False
  def SetNewValue(self, key, value, ex=-1):
    if(ex == -1):
      return self.r.set(key, value, nx=True)
    else :
      return self.r.set(key,value, ex=ex, nx=True)
    
  # 当key存在时才执行修改
  # 修改成功返回True，否则False
  def ReplaceValue(self, key, value, ex=-1):
    if(ex == -1):
      return self.r.set(key, value, xx=True)
    else :
      return self.r.set(key,value, ex=ex, xx=True)
     
  # 批量设置值，keys、values、exs的数组大小必须相等,exs为空的位置需传入-1
  # 调用SetValue设置方式，全部设置成功返回True，否则False
  def SetValueBatch(self, keys, values, exs):
    if((len(keys) != len(values)) or (len(keys) != len(exs))):
      return False
    for index in range(0, len(keys)):
      flag = self.SetValue(keys[index], values[index], ex=exs[index])
      if(flag == False) :
        return False
    return True
  
  # 获取key对应的value
  # 返回值为value
  def GetValue(self, key):
    return self.r.get(key)
  
  # 批量获取值，keys必须为list
  # 返回值为values的list, 获取失败返回False
  def GetValueBatch(self, keys):
    if(type(keys) != list):
      return False
    return self.r.mget(keys)

