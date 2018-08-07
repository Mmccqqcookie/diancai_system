#/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

def open_url(url):
    session = requests.session()
    html = session.get(url)
    html.encoding = 'utf-8'
    return html

def category_dic(url,name_lists):
    html = open_url(url)
    soup = BeautifulSoup(html.text, 'lxml')

    li_list = soup.find('div', class_='category-recipe-list').find('ul', class_='list').find_all('li')
    for li in li_list:
        name = li.find('p', class_='name').find('a').text
        name_lists.append(name.strip())
    # return name_list

def fenlei(category,number_code,):
    name_list = []
    for i in range(1,11):
        if i >= 2:
            url = 'http://www.xiachufang.com/' + 'category' + str(number_code) + '/?page=%s'%str(i)
        else:
            url = 'http://www.xiachufang.com/' + 'category' + str(number_code)
        category_dic(url,name_list)
    return name_list


