# 问题记录

### git使用流程

**开发分支初始化：**

1、`git clone <url>` 克隆远程仓库到本地

2、`git branch -a` 查看所有分支，`git check --track develop`创建develop分支用于开发

3、`git checkout develop`，切换到本地develop分支

4、`git push -u origin develop`将本地的develop分支推送到远程仓库

**新功能开发：**

1、`git checkout origin/develop`切换到远程develop分支，之后的新功能需要在该分支上新建分支开发

2、`git pull`拉取远程develop分支的最新代码

3、`git checkout -b feature/xxx` 创造新的本地特性分支

4、`git push -u origin feature/xxx` 将创建的本地特性分支推送到远程

5、如果远程仓库已经存在feature/xxx分支，那么直接`git checkout -b feature/xxx`即可

6、<在当前特性分支开发>

7、`git add <目录或文件>`将需要更新的文件添加到当前分支

8、`git commit -m '提交说明'`将更新的文件提交

9、推送到远程仓库前使用`git pull --rebase`拉取远程的分支代码（可能有别人提交）

10、`git push`将当前特性分支更新的内容push到远程

**功能测试完成后合并分支：**

1、`git checkout develop`切换到本地develop分支

2、`git pull --rebase`拉取远程develop分支最新代码，

3、`git merge --no-ff feature/xxx`将本地特性分支合并到develop分支上

4、`git push`将合并后的develop分支push到远程

### Python调用Redis

1、服务器安装redis模块：`sudo apt update; sudo apt install redis-server`

2、python安装redis模块：`pip install redis`

[Python redis 使用介绍 | 菜鸟教程](https://www.runoob.com/w3cnote/python-redis-intro.html)

### Python调用本地模块

```python
import os
import sys

now_path = os.getcwd() # 当前路径
add_path = now_path + r"/../conf/" # 需要模块路径
sys.path.append(add_path) # 添加路径

import data_parser # 再import需要模块
```

### Python使用proto

1、python安装protobuf模块包：`pip install protobuf`

2、添加proto文件，需要在先开头声明

```protobuf
syntax = "proto3";
package tag_recommend_system;
```

3、调用命令`protoc --python_out=<pb文件路径> xxx.proto`

会生成一个xxx_pb2.py，就可以引用该py模块

**pb自动生成的序列化和解析函数：**

- SerializeToString()：将message序列化并返回str类型的结果（str类型只是二进制数据的一个容器而已，而不是文本内容）。如果message没有初始化，抛出message.EncodeError异常。

- SerializePartialToString()：将message序列化并返回str类型的结果，但是不检查message是否初始化。

- ParseFromString(data)：从给定的二进制str解析得到message对象。

**数据类型使用：**

- `Enums`：每个枚举对应有value值
- `Message`：每个message的class可能会包含下面的内容：
- `IsInitialized()`：检查是否所有的required 内容都被赋值了
- `__str__()`：会返回一个可读的消息内容，在做debug的时候这个方法就非常有用的
- `CopyFrom(other_msg)`：复制一个message数据过来给，并做新的赋值
- `Clear()`：清空所有元素的value为空

### Python解析yaml

1、安装pyyaml模块：`pip install pyyaml`

```python
import yaml

file = open(file_name, 'r', encoding='utf-8')
file_data = file.read()
file.close()
data = yaml.load(file_data, Loader=yaml.FullLoader) # 读取后的yaml数据
# 其结构是字典套字典
```

### Linux解决git连接慢的问题

原因是global.ssl.fastly.net域名被限制，需要找到该域名对应的ip地址，在hosts上加上ip对应域名的映射，再刷新DNS缓存即可

1、在[IP网](https://www.ipaddress.com/)上搜索域名，得到对应ip

```
http://github.global.ssl.fastly.net
github.co
->
199.232.69.194 github.global-ssl.fastly.net
140.82.112.4 github.com
```

2、在hosts文件末添加上述两行映射：`cd /etc/; sudo vim hosts`

3、保存更新DNS：安装nscd（DNS缓存服务）：`apt install nscd`

然后刷新DNS：`sudo /etc/init.d/nscd restart`

### Python爬虫简单例子

获取网页源码中包含\<head\>到\<script\>的所有内容

```python
url = 'https://fanyi.baidu.com/?aldtype=16047#en/zh/'
content = requests.get(url).content.decode('utf-8')
# print(content)
start = content.find('<head>')
end = content.find('<script>')
content = content[start:end + len('<script>')].strip()
print(content)
```

### Beautiful soup

`pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple beautifulsoup4`

`pip3 install pandas`

`pip install fake_useragent`

`pip install lxml`

### Python命名规范

1、只有类名用驼峰，变量名和函数名都用蛇形

2、函数添加返回值：

```python
def f(a: int, b: int) -> int:
  return a + b
```

3、类里的私有化函数、成员变量：

加上双下划线

4、备注规范：

[python的注释规范 - php、凯 - 博客园](https://www.cnblogs.com/phpk/p/10929039.html)

### Python截取float小数点

### Python对列表里的元组排序

### Python获取调用方名与堆栈帧的帧对象

```python
import sys
def get_cur_info():
  """返回调用方名与堆栈帧的帧对象，用于日志输出"""
  try:
    raise Exception
  except:
    f = sys.exc_info()[2].tb_frame.f_back
  return (str(f.f_code.co_filename) + ':' + str(f.f_code.co_name) + '[' + str(f.f_lineno) + ']' + ': ')
```

### Python Gui

```shell
sudo apt-get install python3-tk
```

### Linux解决端口占用情况

1、查看使用端口号`netstat -ntlp`

2、找到端口号对应的线程pid

3、`kill -9 pid`


