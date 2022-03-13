
from distutils.file_util import move_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
  'user-agent': ua.random,
  'Host': 'movie.douban.com',
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

# 爬取豆瓣top250的电影content，并且解析，返回所有电影解析后的信息
def CrawlDouban(web_config):
  print("crawl douban content!")
  url = web_config['url']
  film_list = []
  # 遍历top250的电影
  for index in range(0,10):
    next_url = url + "?start=" + str(index)
    response = requests.get(next_url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, 'lxml')
    ParseDouban(soup, film_list)
  return film_list

# 解析豆瓣的content，结果加入movie_list
def ParseDouban(soup, film_list):
  div_list = soup.find_all('div', class_='info')
  for each in div_list:
    title = each.find('div', class_='hd').a.span.text.strip()
    each_str = str(each.find('div', class_='hd'))
    url_start_index = each_str.find('href=')
    url_end_index = each_str[:len(each_str)].find(r'/">')
    url = each_str[url_start_index + len(r'href="'):url_end_index + 1].strip()
    rating = each.find('span', class_='rating_num').text.strip()
    try:
        quote = each.find('span', class_='inq').text.strip()
    except:
        quote = ""
    info = each.find('div', class_='bd').p.text.strip()
    info = info.replace("\n", " ").replace("\xa0", " ")
    info = ' '.join(info.split())
    dates = ""
    for c in info:
      if(c.isdigit() == True):
        dates += c
    info_set = info.split(' ' + dates + ' / ')
    try:
      directors_and_actors = info_set[0]
      info_set = info_set[1].split(' / ')
      areas = info_set[0]
      tags = info_set[1].split(' ')
    except:
      directors_and_actors = ""
      areas = ""
      tags = ""
    film_info = {'title':title, 'rating': rating, 'dates': dates, 'tags': tags, 'areas': areas, 'directors_and_actors': directors_and_actors, 'quote': quote}
    # file = open('douban_info', 'a')
    # file.write(film_info) + '\n')
    # file.close()
    
    film_list.append(film_info)
