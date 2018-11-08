# xueqiu_crawl
a crawler of xueqiu 


步骤:
###### 1. 创建雪球爬虫项目
scrapy startproject xueqiu_crawl 
执行结果如下：

You can start your first spider with:
    cd xueqiu_crawl/xueqiu_crawl 
    scrapy genspider example example.com
    
###### 2. 设置mongodb地址 setting.py
``` python 
MONGO_URI="mongodb://root:111111@127.0.0.1:27017" # 设置mongdob地址
```

###### 3.启动爬虫
