# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from db import MongoDB
from items import TopicBriefItem, TopicInfoItem


class XueqiuCrawlPipeline(object):

    def process_item(self, item, spider):
        mongo_ins = MongoDB()
        if isinstance(item, TopicBriefItem):
            if mongo_ins.check_topic_brief_exisit(item.get('target')) is False:
                mongo_ins.topic_brief.insert(dict(item))

        elif isinstance(item, TopicInfoItem):
            if mongo_ins.check_topic_info_exisit(item.get('target')) is False:
                mongo_ins.topic_info.insert(dict(item))

