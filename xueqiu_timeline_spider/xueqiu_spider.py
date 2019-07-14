# -*-coding=utf-8-*-
# 抓取雪球的收藏文章
__author__ = 'Rocky'
import cookielib
import sys
import requests
import json
import time
import os
from urlparse import urljoin
import pymongo

host_url = 'https://xueqiu.com/'
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies")
try:
    session.cookies.load(ignore_discard=True)
except Exception, e :
    print "Cookie can't load"


class MongoDB(object):
    def __init__(self, host, port):
        client = pymongo.MongoClient(host, port)
        xueqiu = client["xueqiu"]
        self.artical = xueqiu["artical"]

mongo_ins = MongoDB('localhost', 27017)






agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {'Host': 'xueqiu.com',
           'Referer': 'https://xueqiu.com/',
           'Origin': 'https://xueqiu.com',
           'User-Agent': agent}
s = session.get(host_url, headers=headers)
session.cookies.save()
time_line_url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id={}&count=20'.format('20310872')
print time_line_url
time_line_response = session.get(time_line_url, headers=headers)
time_line_list = json.loads(time_line_response.text)

for news_info in time_line_list.get('list'):
    data = json.loads(news_info['data'])
    artical_id = data['target']
    artical_url = urljoin(host_url, artical_id)  # 文章地址
    data['artical_url'] = artical_url
    artical_response = session.get(artical_url, headers=headers)
    text = artical_response.text
    data['text'] = text
    print data
    time.sleep(2)












sys.exit(0)
p = re.compile('"maxPage":(\d+)')
maxPage = p.findall(fav_content)[0]
print maxPage
print type(maxPage)
maxPage = int(maxPage)
print type(maxPage)
for i in range(1, maxPage + 1):
    fav = 'https://xueqiu.com/favs?page=%d' % i
    collection = session.get(fav, headers=headers)
    fav_content = collection.text
    # print fav_content
    p = re.compile('var favs = {(.*?)};', re.S | re.M)
    result = p.findall(fav_content)[0].strip()

    new_result = '{' + result + '}'
    # print type(new_result)
    # print new_result
    data = json.loads(new_result)
    use_data = data['list']
    host = 'https://xueqiu.com'
    for i in use_data:
        url = host + i['target']
        print url
        txt_content = session.get(url, headers=headers).text
        # print txt_content.text

        tree = etree.HTML(txt_content)
        title = tree.xpath('//title/text()')[0]

        filename = re.sub('[\/:*?"<>|]', '-', title)
        print filename

        content = tree.xpath('//div[@class="detail"]')
        Toolkit.save2filecn(filename, "Link: %s\n\n" % url)
        for i in content:
            Toolkit.save2filecn(filename, i.xpath('string(.)'))
        # print content
        # Toolkit.save2file(filename,)
        time.sleep(10)
