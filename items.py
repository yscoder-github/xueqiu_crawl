# encoding=utf-8
# ------------------------------------------
#   版本：1.0
#   日期：2018-10-17
#   作者：殷帅
# ------------------------------------------

from scrapy import Item, Field


class TopicBriefItem(Item):
    """话题信息"""
    feedback = Field()
    pic = Field()  # 图片
    reply_count = Field()  # 回复数
    id = Field()  # id
    topic_pic = Field()
    title = Field()
    first_pic = Field()
    cover_pic = Field()
    source = Field()
    link_stock_desc = Field()
    score = Field()
    retweet_count = Field()
    topic_pic_hd = Field()
    description = Field()
    reweeted_status = Field()
    view_count = Field()
    quote_cards = Field()
    topic_title = Field()  # 话题标题
    user_profile = Field()  # 用户主页
    target = Field()  # 文章地址
    created_at = Field()  # 文章创建时间
    promotion = Field()
    tag = Field()
    link_stock_symbol = Field()
    topic_desc = Field()  # 话题描述


class TopicInfoItem(Item):
    """话题详情"""
    target = Field()  # 文章地址
    text = Field()  # 网页文本
