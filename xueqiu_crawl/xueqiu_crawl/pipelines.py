# -*- coding: utf-8 -*-
# ------------------------------------------
#   版本：1.0
#   日期：2018-10-13
#   作者：殷帅　yscoder@foxmail.com
# ------------------------------------------
# Define my item pipelines here
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
        else:
            raise ValueError("unknown item instance")

