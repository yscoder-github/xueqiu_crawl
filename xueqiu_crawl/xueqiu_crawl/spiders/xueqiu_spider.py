#!/usr/bin/python
# -*-coding:utf-8-*-
"""
In this module, you can find the XueQiuSpider class.
It is a spider to crawl the xueqiu network
"""

from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider, Rule
from scrapy.utils import log


# from xueqiu_crawler.items import XueQiuCrawlerItem
# from xueqiu_crawler.utils.select_result import list_first_item, strip_null, deduplication, clean_url


class XueQiuSpider(Spider):
    name = "xueqiu"
    start_urls = (
        'https://xueqiu.com/',
    )

    def parse_login(self, response):
        print response.text
        yield Request("https://xueqiu.com/v4/statuses/public_timeline_by_category.json",
                      # headers=self.headers,
                      callback=self.calltest)

    def parse(self, response):
        if response.url is not 'https://xueqiu.com':
            print response.text
        yield Request("https://xueqiu.com/v4/statuses/public_timeline_by_category.json",
                      callback=self.parse)

        """ 
        Parse a response. This new version yields every request
        gotten by following links on a page into a LinkItem.
        This place,responce is the url response html, and response.url is the url from the .. 

        """
        """
        for request_or_item in super(XueQiuSpider, self).parse(response):
            print request_or_item
            continue
            if isinstance(request_or_item, Request):
                # print '--------------------'
                # print 'target is ',request_or_item.url
                # print 'source is ',response.url
                # print 'anchor is ',request_or_item.meta['link_text'],'\n'
                yield LinkItem(target=request_or_item.url,
                               source=response.url,
                               anchor=request_or_item.meta['link_text'])
                # time.sleep(0.3)
            yield request_or_item
        """
        """
        next_link = list_first_item(response_selector.select(u'//div[@class="k2"]/div/a[text()="下一页"]/@href').extract())
        if next_link:
            next_link = clean_url(response.url, next_link, response.encoding)
            yield Request(url=next_link, callback=self.parse)

        for detail_link in response_selector.select(u'//div[contains(@class,"sousuolist")]/a/@href').extract():
            if detail_link:
                detail_link = clean_url(response.url, detail_link, response.encoding)
                yield Request(url=detail_link, callback=self.parse_detail)
        """
    def jsontreat(self, response):
        print response.text






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
