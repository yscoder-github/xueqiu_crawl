#!/usr/bin/python
# -*-coding:utf-8-*-
"""
In this module, you can find the XueQiuSpider class.
It is a spider to crawl the xueqiu network
author: yscoder@foxmail.com
"""

from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider, Rule
from urlparse import urljoin, urlparse
import json
import logging
logger = logging.getLogger(__name__)


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
            print code
            if next_max_id == -1 or topic_list == []:
                return
            for topic in topic_list:
                topic_brief_url = urljoin(self._host_url, json.loads(topic.get('data')).get('target'))
                yield Request(topic_brief_url, callback=self.parse_response)
            yield Request(self._topic_url.format(next_max_id, code),
                          meta={'code': code},
                          callback=self.parse_request)
        except:
            raise

    def parse(self, response):
        for code in self._category:
            topic_url = self._topic_url.format(-1, code)
            yield Request(topic_url,
                          meta={'code': code},
                          callback=self.parse_request)


    def parse_response(self, response):
        pass


    def on_idle(self, spider):
        """ Called when no more requests is in the queue and no more item
        is remaining in the pipeline """
        # spider.compute_pagerank()
        pass

    """
    def parse_detail(self, response):
        woaidu_item = WoaiduCrawlerItem()

        response_selector = HtmlXPathSelector(response)
        woaidu_item['book_name'] = list_first_item(
            response_selector.select('//div[@class="zizida"][1]/text()').extract())
        woaidu_item['author'] = [
            list_first_item(response_selector.select('//div[@class="xiaoxiao"][1]/text()').extract())[5:].strip(), ]
        woaidu_item['book_description'] = list_first_item(
            response_selector.select('//div[@class="lili"][1]/text()').extract()).strip()
        woaidu_item['book_covor_image_url'] = list_first_item(
            response_selector.select('//div[@class="hong"][1]/img/@src').extract())

        download = []
        for i in response_selector.select('//div[contains(@class,"xiazai_xiao")]')[1:]:
            download_item = {}
            download_item['url'] = \
                strip_null( \
                    deduplication( \
                        [ \
                            list_first_item(i.select('./div')[0].select('./a/@href').extract()), \
                            list_first_item(i.select('./div')[1].select('./a/@href').extract()) \
                            ] \
                        ) \
                    )

            download_item['progress'] = list_first_item(i.select('./div')[2].select('./text()').extract())
            download_item['update_time'] = list_first_item(i.select('./div')[3].select('./text()').extract())
            download_item['source_site'] = \
                [ \
                    list_first_item(i.select('./div')[4].select('./a/text()').extract()), \
                    list_first_item(i.select('./div')[4].select('./a/@href').extract()) \
                    ] \
 \
            download.append(download_item)

        woaidu_item['book_download'] = download
        woaidu_item['original_url'] = response.url

        yield woaidu_item
        """
