# xueqiu_crawl
a distribute crawler of xueqiu 


步骤:
######1 创建雪球爬虫项目
scrapy startproject xueqiu_crawl 
执行结果如下：
New Scrapy project 'xueqiu_crawl', using template directory '/usr/local/lib/python2.7/dist-packages/scrapy/templates/project', created in:
    /home/yinshuai/code/nlp/xueqiu_crawl/xueqiu_crawl

You can start your first spider with:
    cd xueqiu_crawl
    scrapy genspider example example.com
    
    
    
# 添加到主分支
添加所有文件至暂存区
$ git add .
提交所有文件至本地仓库
$ git commit -m 'create xueqiu_crawl project'
推送提交至远程仓库
$ git push origin master


雪球主页：https://xueqiu.com/　　一个财经网站　


### 下面是代理的使用方法
Random proxy middleware for Scrapy (http://scrapy.org/)
=======================================================

Processes Scrapy requests using a random proxy from list to avoid IP ban and
improve crawling speed.

Get your proxy list from sites like http://www.hidemyass.com/ (copy-paste into text file
and reformat to http://host:port format)

Install
--------

The quick way:

    pip install scrapy_proxies

Or checkout the source and run

    python setup.py install


settings.py
-----------

    # Retry many times since proxies often fail
    RETRY_TIMES = 10
    # Retry on most error codes since proxies fail for different reasons
    RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
        'scrapy_proxies.RandomProxy': 100,
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    }

    # Proxy list containing entries like
    # http://host1:port
    # http://username:password@host2:port
    # http://host3:port
    # ...
    PROXY_LIST = '/path/to/proxy/list.txt'
    
    # Proxy mode
    # 0 = Every requests have different proxy
    # 1 = Take only one proxy from the list and assign it to every requests
    # 2 = Put a custom proxy to use in the settings
    PROXY_MODE = 0
    
    # If proxy mode is 2 uncomment this sentence :
    #CUSTOM_PROXY = "http://host1:port"


For older versions of Scrapy (before 1.0.0) you have to use
scrapy.contrib.downloadermiddleware.retry.RetryMiddleware and
scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware
middlewares instead.


Your spider
-----------

In each callback ensure that proxy /really/ returned your target page by
checking for site logo or some other significant element.
If not - retry request with dont_filter=True

    if not hxs.select('//get/site/logo'):
        yield Request(url=response.url, dont_filter=True)










