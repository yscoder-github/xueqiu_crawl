# -*- coding: utf-8 -*-
# ------------------------------------------
#   版本：1.0
#   日期：2018-10-13
#   作者：殷帅　yscoder@foxmail.com
# ------------------------------------------
import pymongo
from toolkit import singleton

@singleton
class MongoDB(object):
    """Mongodb单例"""
    def __init__(self):
        self.mongo_uri = "mongodb://127.0.0.1:27017"
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client['Topic']
        self.topic_brief = self.db.topic_brief
        self.topic_info = self.db.topic_info

    def check_topic_brief_exisit(self, target):
        """ 判断是否当前已经存在该数据"""
        cnt = self.topic_brief.find({"target": target}).count()
        return True if cnt >= 1 else False

    def check_topic_info_exisit(self, target):
        """ 判断是否当前已经存在该数据"""
        cnt = self.topic_info.find({"target": target}).count()
        return True if cnt >= 1 else False


