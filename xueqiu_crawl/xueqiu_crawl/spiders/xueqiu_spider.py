#!/usr/bin/python
# -*-coding:utf-8-*-
"""
In this module, you can find the XueQiuSpider class.
It is a spider to crawl the xueqiu network
"""

from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider, Rule
from scrapy.linkextractors import LinkExtractor
# from xueqiu_crawler.items import XueQiuCrawlerItem
# from xueqiu_crawler.utils.select_result import list_first_item, strip_null, deduplication, clean_url


class XueQiuSpider(Spider):
    name = "xueqiu"
    start_urls = (
        # 'https://xueqiu.com/',
        'https://xueqiu.com/v4/statuses/public_timeline_by_category.json',
    )


    def __init__(self):
        self.headers = {
            'Accept-Language': ' zh-CN,zh;q=0.9', 'Accept-Encoding': ' gzip, deflate, br',
            'X-Requested-With': ' XMLHttpRequest', 'Host': ' xueqiu.com', 'Accept': ' */*',
            'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
            'Connection': ' keep-alive',
            'Pragma': ' no-cache', 'Cache-Control': ' no-cache', 'Referer': ' https://xueqiu.com/u/1955602780'

        }

        # self.cookies={'Cookie': ' device_id=f174304eb593fc036db5db25d3124fad; s=e31245o8yi; bid=a8ec0ec01035c8be5606c595aed718d4_j9xsz38j; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=f57a2e24d323f2c27ec40d3ac26ee9a10e1857dc; xq_a_token.sig=-3diSs4C6X4-m1mC-h618cAeWj4; xq_r_token=7ceedf9c41c4b6d4054d6f25c1ca3087e40483a2; xq_r_token.sig=XtalVKjjXjLzRRBR0HwHAjfH3N0; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=1733473480; u.sig=2sMTnVmBVOASyCZs6lbVBQ6Zfgs; __utmz=1.1524820182.167.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; aliyungf_tc=AQAAACK8rRyK8gYAAyAmG3lNK4rFWjui; __utma=1.8758030.1510556188.1525936226.1526117855.176; __utmc=1; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1525403929,1525410601,1525929687,1526117855; __utmb=1.5.10.1526117855; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1526117884; snbim_minify=true'}
        # self.cookies={'Cookie':'device_id=f174304eb593fc036db5db25d3124fad; s=e31245o8yi; bid=a8ec0ec01035c8be5606c595aed718d4_j9xsz38j; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=f57a2e24d323f2c27ec40d3ac26ee9a10e1857dc; xq_a_token.sig=-3diSs4C6X4-m1mC-h618cAeWj4; xq_r_token=7ceedf9c41c4b6d4054d6f25c1ca3087e40483a2; xq_r_token.sig=XtalVKjjXjLzRRBR0HwHAjfH3N0; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=1733473480; u.sig=2sMTnVmBVOASyCZs6lbVBQ6Zfgs; __utmz=1.1524820182.167.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; aliyungf_tc=AQAAACK8rRyK8gYAAyAmG3lNK4rFWjui; __utma=1.8758030.1510556188.1525936226.1526117855.176; __utmc=1; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1525403929,1525410601,1525929687,1526117855; __utmb=1.5.10.1526117855; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1526117884; snbim_minify=true'}
        self.cookies = {"device_id": "f174304eb593fc036db5db25d3124fad",
                        "s": "e31245o8yi",
                        "bid": "a8ec0ec01035c8be5606c595aed718d4_j9xsz38j",
                        "remember": "1",
                        "remember.sig": "K4F3faYzmVuqC0iXIERCQf55g2Y",
                        "xq_a_token": "f57a2e24d323f2c27ec40d3ac26ee9a10e1857dc",
                        "xq_a_token.sig": "-3diSs4C6X4-m1mC-h618cAeWj4",
                        "xq_r_token": "7ceedf9c41c4b6d4054d6f25c1ca3087e40483a2",
                        "xq_r_token.sig": "XtalVKjjXjLzRRBR0HwHAjfH3N0",
                        "xq_is_login": "1",
                        "xq_is_login.sig": "J3LxgPVPUzbBg3Kee_PquUfih7Q",
                        "u": "1733473480",
                        "u.sig": "2sMTnVmBVOASyCZs6lbVBQ6Zfgs",
                        "__utmz": "1.1524820182.167.7.utmcsr",
                        "aliyungf_tc": "AQAAACK8rRyK8gYAAyAmG3lNK4rFWjui",
                        "__utma": "1.8758030.1510556188.1525936226.1526117855.176",
                        "__utmc": "1",
                        "__utmt": "1",
                        "Hm_lvt_1db88642e346389874251b5a1eded6e3": "1525403929,1525410601,1525929687,1526117855",
                        "__utmb": "1.5.10.1526117855",
                        "Hm_lpvt_1db88642e346389874251b5a1eded6e3": "1526117884",
                        "snbim_minify": "true"
                        }

    def start_requests(self):
        count = 20
        userid = 1955602780
        # maxPage = 2
        maxPage = 1796
        base_url = 'https://xueqiu.com/v4/statuses/user_timeline.json?page={}&user_id={}'
        for pn in range(1, maxPage + 1):
            url = base_url.format(pn, userid)
            print url

            yield Request(url, cookies=self.cookies, headers=self.headers)





    def __init222__(self, *args, **kwargs):
        self.rules = [Rule(self.get_link_extractor(),
                           # callback=self.parse_item,
                           # process_links=self.limit_links,
                           follow=True)]
        super(XueQiuSpider, self).__init__(*args, **kwargs)

        """
        target_sites = settings.get('TARGET_SITES')
        if target_sites and os.path.isfile(target_sites):
            # Read a list of URLs from file
            # Create the target file list
            with open(target_sites) as target_sites_file:
                # Make it to Python list
                self.start_urls = target_sites_file.read().splitlines()
                # Remove empty strings
                self.start_urls = [u for u in self.start_urls if u]
        else:
            self.start_urls = self.default_start_url
        """
    """
    link_extractor is a Link Extractor object which defines how links will be extracted
      from each crawled page.
    """
    def get_link_extractor(self):
        return LinkExtractor(allow_domains=['https://xueqiu.com/'])


    """
    The parse() method will be called to handle each of the requests for those STARTURLs,
    even though we haven’t explicitly told Scrapy to do so. This happens because
    parse() is Scrapy’s default start_url callback method, which is called for requests without
    an explicitly assigned callback.
    This method, as well as any other Request callback, must return an iterable of 
    Request and/or dicts or Item objects.
    shuai: i think the response contains the html content of the specify url and we even 
           can use response.url to get the current url.keep in mind,response is an object.
    In callback functions, you parse the page contents, typically using Selectors (but you 
    can also use BeautifulSoup, lxml or whatever mechanism you prefer) and generate items 
    with the parsed data.
    """

    def parse(self, response):
        response_selector = Selector(response)
        print response_selector.xpath(r"*").extract()
        pass
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
