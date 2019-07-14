#!/usr/bin/python
# -*-coding:utf-8-*-
"""
In this module, you can find the XueQiuSpider class.
It is a spider to crawl the xueqiu network
author: yscoder@foxmail.com
"""

from scrapy.http import Request
from scrapy.spiders import Spider
# from xueqiu_relation_crawler.items import TopicBriefItem, TopicInfoItem
from urlparse import urljoin, urlparse
import json
import logging
logger = logging.getLogger(__name__)


class XueQiuSpider(Spider):


    name = "xueqiu_relation_crawler"
    _relation_url = \
        "https://xueqiu.com/friendships/followers.json?uid={}&pageNo={}"

    _host_url = 'https://xueqiu.com/'
    start_urls = (
       _host_url,
    )

    def parse_request(self, response):
        try:
            json_data = json.loads(response.text)
            count = json_data['count']  # 关注总总数
            max_page = json_data['page']  # 最大页数
            follower_list = json_data['followers']
            # print follower_list
            for follower in follower_list:
                print follower


            #     yield topic_item  # 存储
            #     yield Request(topic_brief_url, callback=self.parse_response)   # 发出请求
            # yield Request(self._topic_url.format(next_max_id, code),
            #               meta={'code': code},
            #               callback=self.parse_request)
        except:
            raise

    def parse(self, response):
            uid = '1287305957'
            page_num = 1
            relation_url = self._relation_url.format(uid, 1)
            yield Request(relation_url,
                          callback=self.parse_request)

    def parse_response(self, response):
        """存储用户信息"""
        pass
        # target = urlparse(response.url).path  # 获取文章地址
        # topic_info_item = TopicInfoItem()
        # topic_info_item['target'] = target
        # topic_info_item['text'] = response.text
        # yield topic_info_item




    def on_idle(self, spider):
        """ Called when no more requests is in the queue and no more item
        is remaining in the pipeline """
        # spider.compute_pagerank()
        pass


