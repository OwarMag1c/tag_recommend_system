## 开发环境

server开发环境为Ubuntu 20.04，client开发环境为Windows10 64bits。

服务端使用Python版本为3.8.10，客户端使用Python版本为3.10.1。

## 客户端环境

安装Python3.10.1

[Download Python | Python.org](https://www.python.org/downloads/)

## 服务端环境

```shell
# server端python安装
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3

# server端Ubuntu python库安装
sudo pip3 install redis
sudo pip3 install UserAgent
sudo apt-get install Python-bs4
sudo pip3 install protobuf

# server端Ubuntu redis安装
sudo apt update
sudo apt install redis-server
```

## 客户端应用打包exe

```shell
# /client下运行
pip3 install pyinstaller
Pyinstaller -F -w gui_test.py
```

## 客户端运行

windows 64bits下运行/client/dist/电影推荐.exe

## 服务端运行

```shell
cd /server
python3 tag_recommend_system_server.py
```

