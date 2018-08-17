#/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import time
from Service.caimenu.ServiceCaiMenu import CaiMenu_Service

category = {
    '/category/40076':1,
    '/category/40078':2,
    '/category/51848':3,
    '/category/52354':4,
    '/category/20130':5,
    '/category/20137':6

}
cate_dish ={
    'jiachangcai':1,
    'xiafancai':2,
    'sucai':3,
    'dayudarou':4,
    'tanggeng':5,
    'liangcai':6
}

def open_url_keword(keyword):
    data = {'keyword':keyword,'cat':1001}
    session = requests.session()
    html = session.get('http://www.xiachufang.com/search/?',params=data)
    html.encoding = 'utf-8'
    return html


def open_url(url):
    session = requests.session()
    html = session.get(url)
    html.encoding = 'ut-8'
    return html


def get_keyword_step(url):
    html = open_url(url)

    soup = BeautifulSoup(html.text,'lxml')

    steps = soup.find('div',class_='steps').find_all('p')
    steps = list(steps)
    for i in steps:
        print(i)
    print(type(steps),steps)
    step = ' '.join(steps)
    return  steps

def page_tab_data(url,category_url):
    html = open_url(url)
    soup = BeautifulSoup(html.text, 'lxml')
    if soup.select('.search-result-list'):
        search_list = soup.find('div',class_='search-result-list').find('ul',class_='list').find_all('li')
    else:
        search_list = soup.find('div',class_='normal-recipe-list').find('ul', class_='list').find_all('li')
    search_detail = []
    for li in search_list:
        title = li.find('p', class_='name').find('a').text.strip().split(' ')[0]
        url = 'http://www.xiachufang.com' + li.find('p', class_='name').find('a')['href'].strip()
        side_dish = li.find('p', class_='ing ellipsis').text.strip()
        img = li.find('img')['data-src'].strip()
        stats = str(li.find('p', class_='stats')).strip()
        add_caidan = CaiMenu_Service()
        response = add_caidan.check_dish_exits(title)
        if not response.status:
            add_caidan.add_dish(title, url, img, side_dish, stats, category[category_url])
        dish_detail = {'title': title, 'url': url, 'img': img,
                       'side_dish': side_dish, 'stats': str(stats)}
        search_detail.append(dish_detail)
    return search_detail


def get_search_html(keyword,perfect_match=False,cate=None):
    html = open_url_keword(keyword.strip())
    response_url = html.url.replace('http://www.xiachufang.com','')
    soup = BeautifulSoup(html.text,'lxml')
    if soup.select('.search-result-list'):
        search_list = soup.find('div',class_='search-result-list').find('ul',class_='list').find_all('li')
    else:
        search_list = soup.find('div',class_='normal-recipe-list').find('ul', class_='list').find_all('li')
    search_detail = []
    for li in search_list:
        title = li.find('p',class_='name').find('a').text
        url = 'http://www.xiachufang.com' + li.find('p',class_='name').find('a')['href']
        side_dish = li.find('p',class_='ing ellipsis').text
        img = li.find('img')['data-src']
        stats = str(li.find('p',class_='stats'))
        dish_detail = {'title':title,'url':url,'img':img,
                       'side_dish':side_dish,'stats':stats}
        if perfect_match:
            if keyword.strip() == title.strip():
                add_caidan = CaiMenu_Service()
                add_caidan.add_dish(title, url, img, side_dish, stats, cate_dish[cate])
                return dish_detail
        search_detail.append(dish_detail)
    return search_detail,response_url



