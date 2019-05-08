#!/usr/bin/python3
# -*-coding:utf-8-*-
"""
In this module, you can find the XueQiuSpider class.
It is a spider to crawl the xueqiu network
author: yscoder@foxmail.com
"""

from scrapy.http import Request
from scrapy.spiders import Spider
from xueqiu_crawl.items import TopicBriefItem, TopicInfoItem
from urllib.parse import urlparse, urljoin
import json
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='debug.log',
                    filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


class XueQiuSpider(Spider):


    name = "xueqiu"
    _topic_url = \
        "https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id={}&count=20&category={}"
    
    _host_url = 'https://xueqiu.com/'
    start_urls = (
       _host_url,
    )
    _category = {
        '-1': "头条",
        '6': "直播",
        '105': "沪深",
        '111': "房产",
        '102': "港股",
        '104': "基金",
        '101': "美股",
        '113': "私募",
        '114': "机车",
        '110': "保险"
    }

    def parse_request(self, response):
        try:
            json_data = json.loads(response.text)
            next_max_id = json_data.get('next_max_id', -1)
            topic_list = json_data.get('list', [])
            code = response.meta['code']



            info =  '{}{}'.format(code, next_max_id)
            logger.info(info)
            return
            if next_max_id == -1 or topic_list == []:
                return
            for topic in topic_list:
                topic_item = TopicBriefItem()
                data = json.loads(topic.get('data'))
                topic_brief_url = urljoin(self._host_url, data.get('target'))
                topic_item['feedback'] = data.get('feedback')
                topic_item['pic'] = data.get('pic')
                topic_item['reply_count'] = data.get('reply_count')
                topic_item['id'] = data.get('id')
                topic_item['topic_pic'] = data.get('topic_pic')
                topic_item['title'] = data.get('title')
                topic_item['first_pic'] = data.get('first_pic')
                topic_item['cover_pic'] = data.get('cover_pic')
                topic_item['source'] = data.get('source')
                topic_item['link_stock_desc'] = data.get('link_stock_desc')
                topic_item['score'] = data.get('score')
                topic_item['retweet_count'] = data.get('retweet_count')
                topic_item['topic_pic_hd'] = data.get('topic_pic_hd')
                topic_item['description'] = data.get('description')
                topic_item['reweeted_status'] = data.get('reweeted_status')
                topic_item['view_count'] = data.get('view_count')
                topic_item['quote_cards'] = data.get('quote_cards')
                topic_item['topic_title'] = data.get('topic_title')
                topic_item['user_profile'] = data.get('profile')
                topic_item['target'] = data.get('target')
                topic_item['created_at'] = data.get('created_at')
                topic_item['promotion'] = data.get('promotion')
                topic_item['tag'] = data.get('tag')
                topic_item['link_stock_symbol'] = data.get('link_stock_symbol')
                topic_item['topic_desc'] = data.get('topic_desc')
                yield topic_item  # 存储
                yield Request(topic_brief_url, callback=self.parse_response)   # 发出请求
            yield Request(self._topic_url.format(next_max_id, code),
                          meta={'code': code},
                          callback=self.parse_request)
        except Exception as  e:
            logger.exception(e)

    def parse(self, response):
        for code in self._category:
            topic_url = self._topic_url.format(-1, code)
            yield Request(topic_url,
                          meta={'code': code},
                          callback=self.parse_request)

    def parse_response(self, response):
        """解析文章内容"""
        target = urlparse(response.url).path  # 获取文章地址
        topic_info_item = TopicInfoItem()
        topic_info_item['target'] = target
        topic_info_item['text'] = response.text
        yield topic_info_item




    def on_idle(self, spider):
        """ Called when no more requests is in the queue and no more item
        is remaining in the pipeline """
        # spider.compute_pagerank()
        pass
