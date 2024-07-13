# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
    定义数据类型
"""

class Hot_Topic_Item(scrapy.Item):
    # - 热门话题ID
    topic_id = scrapy.Field()
    # - 热门话题
    topic_name = scrapy.Field()
    # - 热门话题对应博文链接
    topic_link = scrapy.Field()
    # - 话题热门指数
    topic_num = scrapy.Field()
    # - 话题排行
    topic_rank = scrapy.Field()
    # - 爬取热门话题时间
    topic_time = scrapy.Field()

    # - 话题下所有博文（后期在数据库中存储时，使用一对多的关系，在博文数据库中存储其热点话题的主键）

class Topic_Detail_Item(scrapy.Item):
    # 1. 热点话题名称
    topic_name = scrapy.Field()
    # 2. 热点话题ID
    topic_id = scrapy.Field()
    # 2.1. 热点话题location
    topic_location = scrapy.Field()
    # 3. 热点话题分类
    topic_category = scrapy.Field()
    # 4. 话题导语
    topic_introduction = scrapy.Field()
    # 5. 热点话题主持人名称
    topic_host = scrapy.Field()
    # 6. 话题阅读数
    topic_read_num = scrapy.Field()
    # 7. 话题讨论次数
    topic_talk_num = scrapy.Field()
    # 8. 话题博文原创人数
    topic_original_num = scrapy.Field()
    # 9. 阅读趋势
    topic_read_trend = scrapy.Field()
    # 10. 讨论趋势
    topic_talk_trend = scrapy.Field()
    # 11. 原创人数趋势
    topic_original_trend = scrapy.Field()

class Update_Topic_Detail_Item(scrapy.Item):
    # 2. 热点话题ID
    topic_id = scrapy.Field()
    # 3. 阅读趋势
    topic_read_trend = scrapy.Field()
    # 4. 讨论趋势
    topic_talk_trend = scrapy.Field()
    # 5. 原创人数趋势
    topic_original_trend = scrapy.Field()

class Update_Topic_Detail_Num_Item(scrapy.Item):
    # 2. 热点话题ID
    topic_id = scrapy.Field()
    # 3. 阅读数
    topic_read_num = scrapy.Field()
    # 4. 讨论数
    topic_talk_num = scrapy.Field()
    # 5. 原创人数
    topic_original_num = scrapy.Field()

class Topic_Article_Item(scrapy.Item):
    # 0. 热点话题名称
    topic_id = scrapy.Field()
    # 1. 热点话题名称
    topic_name = scrapy.Field()
    # 2. 话题导语
    topic_introduction = scrapy.Field()
    # 3. 作者昵称：.//div[@class='info']//a/@nick-name
    author_name = scrapy.Field()
    # 4. 作者uid：从头像的超链接处获得
    author_id = scrapy.Field()
    # 5. 发文时间：.//p[@class='from']
    article_time = scrapy.Field()
    # 6. 博文正文链接：.//p[@class='from']/a[1]/@href
    article_link = scrapy.Field()
    # 7. 每个博文的ID
    article_id = scrapy.Field()
    # 8. 热搜榜对应博文卡片的mid
    article_mid = scrapy.Field()
    # 9. 获取show链接，该请求链接可获得json数据，其中包括 isLongText 属性，其标志是否为长文
    article_show_link = scrapy.Field()
    # 10. 获取评论的请求链接
    article_comment_link = scrapy.Field()
    # 11. 获取长文链接
    article_longText_link = scrapy.Field()

class Article_Detail_Item(scrapy.Item):
    # 0. 博文ID
    article_id = scrapy.Field()
    # 1. 微博正文
    article_content = scrapy.Field()
    # 2. 转发数
    num_forward = scrapy.Field()
    # 3. 评论数
    num_comment = scrapy.Field()
    # 4. 点赞数
    num_like = scrapy.Field()
    # 5. 作者昵称
    author_name = scrapy.Field()
    # 6. 发文时间
    article_time = scrapy.Field()
    # 7. 评论
    comment_data = scrapy.Field()

class Article_Comment_Item(scrapy.Item):
    # - 博文ID
    article_id = scrapy.Field()
    # - 评论时间
    comment_time = scrapy.Field()
    # - 评论ID
    comment_id = scrapy.Field()
    # - 评论内容
    comment_content = scrapy.Field()
    # - 评论人所在省份
    comment_province = scrapy.Field()
    # - 评论人ID
    comment_author_id = scrapy.Field()
    # - 评论人名称
    comment_author_name = scrapy.Field()
