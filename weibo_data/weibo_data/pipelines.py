# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import codecs
import csv
import pymysql
import uuid

# 改变标准输出的默认编码
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

from .items import *

# class WeiboDataPipeline:
#     # # 自定义json文件的导出
#     def __init__(self):  # 初始化，打开文件
#         self.file = codecs.open('weibo_detail.json', 'w', encoding="utf-8")
#         # 这里用codecs库来打开文件，目的是编码不会出错
#
#     def process_item(self, item, spider):  # 写入文件
#         if spider.name == 'weibo':
#             lines = json.dumps(dict(item), ensure_ascii=False) + ",\n"
#             self.file.write(lines)
#         return item
#
#     def spider_closed(self, spider):  # 关闭文件
#         self.file.close()
#
# # 数据存储在csv文件里
# class savefileTongscrapyPipeline(object):
#     def __init__(self):
#         self.file = open('weibo_detail.csv', 'w', newline='')
#         self.csvwriter = csv.writer(self.file)
#         self.csvwriter.writerow(['话题名称', '话题导语', '博文作者名称', '发表时间', '博文链接', '作者ID', '博文卡片ID', 'article_show_link', 'article_comment_link', 'article_longText_link'])
#
#     def process_item(self, item, spider):
#         if spider.name == 'weibo':
#             self.csvwriter.writerow([item["topic_name"],item["topic_introduction"],item["author_name"],item["article_time"],item["article_link"], item["author_id"], item["article_mid"], item["article_show_link"], item["article_comment_link"], item["article_longText_link"]])
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()

# 数据存储在MySQL数据库里

""" 持久化微博话题热榜 """
class SaveToMysqlDB_HotTopicItem_Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='weibo_scrapy_data',  # 数据库名
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.conn.cursor()
        print("数据库连接成功，准备写入hot_topic")

    def process_item(self, item, spider):
        if isinstance(item, Hot_Topic_Item):  # 判断item是否为Hot_Topic_Item类型
            # sql语句，向 hot_topic 表中插入数据
            insert_sql = 'insert into hot_topic(id, topic_id, topic_name, topic_link, topic_num, topic_rank, topic_time) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(
                insert_sql,
                (
                    # 通过uuid库获取唯一ID
                    uuid.uuid1().hex,
                    item["topic_id"],
                    item["topic_name"],
                    item["topic_link"],
                    item["topic_num"],
                    item["topic_rank"],
                    item["topic_time"]
                )
            )
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
            print("数据已保存到mysql_hot_topic")
        # 此处的 return 不能删除，因为后面的管道会接收该item，
        # 否则 后面的管道 中的item为空
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

""" 持久化每个热点话题的详情信息 """
class SaveToMysqlDB_TopicDetailItem_Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='weibo_scrapy_data',  # 数据库名
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.conn.cursor()
        print("数据库连接成功，准备写入article_comment")

    def process_item(self, item, spider):
        # 判断item是否为Topic_Detail_Item类型
        if isinstance(item, Topic_Detail_Item):
            # sql语句，向 topic_detail 表中插入数据
            insert_sql = 'insert into topic_detail(' \
                         'id,' \
                         'topic_id,' \
                         'topic_name,' \
                         'topic_location,' \
                         'topic_category,' \
                         'topic_introduction,' \
                         'topic_host,' \
                         'topic_read_num,' \
                         'topic_talk_num,' \
                         'topic_original_num,' \
                         'topic_read_trend,' \
                         'topic_talk_trend,' \
                         'topic_original_trend) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(
                insert_sql,
                (
                    # 通过uuid库获取唯一ID
                    uuid.uuid1().hex,
                    item["topic_id"],
                    item["topic_name"],
                    item["topic_location"],
                    item["topic_category"],
                    item["topic_introduction"],
                    item["topic_host"],
                    item["topic_read_num"],
                    item["topic_talk_num"],
                    item["topic_original_num"],
                    item["topic_read_trend"],
                    item["topic_talk_trend"],
                    item["topic_original_trend"]
                )
            )
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
            print("数据已保存到mysql_topic_detail")
        return item  # 返回item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

""" 更新话题详情中的 阅读趋势、原创趋势、讨论趋势 数据 """
""" 持久化每个热点话题的详情信息 """
class Update_TopicDetailItem_Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='weibo_scrapy_data',  # 数据库名
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.conn.cursor()
        print("数据库连接成功，准备写入article_comment")

    def process_item(self, item, spider):
        # 判断item是否为 Update_Topic_Detail_Item 类型
        if isinstance(item, Update_Topic_Detail_Item):
            # sql语句，向 topic_detail 表中插入数据
            update_sql = 'update topic_detail set ' \
                         'topic_read_trend=%s,' \
                         'topic_talk_trend=%s,' \
                         'topic_original_trend=%s where topic_id=%s'
            self.cursor.execute(
                update_sql,
                (
                    # 通过uuid库获取唯一ID
                    item["topic_read_trend"],
                    item["topic_talk_trend"],
                    item["topic_original_trend"],
                    item["topic_id"]
                )
            )
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
            print("数据已更新到topic_detail")
        return item  # 返回item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

""" 更新话题详情中的 阅读趋势、原创趋势、讨论趋势 数据 """
""" 持久化每个热点话题的详情信息 """
class Update_TopicReadNum_Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='weibo_scrapy_data',  # 数据库名
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.conn.cursor()
        print("数据库连接成功，准备写入article_comment")

    def process_item(self, item, spider):
        # 判断item是否为 Update_Topic_Detail_Num_Item 类型
        if isinstance(item, Update_Topic_Detail_Num_Item):
            # sql语句，向 topic_detail 表中插入数据
            update_sql = 'update topic_detail set ' \
                         'topic_read_num=%s,' \
                         'topic_talk_num=%s,' \
                         'topic_original_num=%s where topic_id=%s'
            self.cursor.execute(
                update_sql,
                (
                    # 通过uuid库获取唯一ID
                    item["topic_read_num"],
                    item["topic_talk_num"],
                    item["topic_original_num"],
                    item["topic_id"]
                )
            )
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
            print("数据已更新到topic_detail_num")
        return item  # 返回item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

""" 持久化每个话题下的简要博文信息 """
class SaveToMysqlDB_TopicArticleItem_Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='weibo_scrapy_data',  # 数据库名
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.conn.cursor()
        print("数据库连接成功，准备写入topic_article")

    def process_item(self, item, spider):
        if isinstance(item, Topic_Article_Item):  # 判断item是否为Topic_Article_Item类型
            # print("Topic_Article_Item: ",item)
            # sql语句，向 topic_article 表中插入数据
            insert_sql = 'insert into topic_article(' \
                         'id, ' \
                         'topic_id, ' \
                         'topic_name, ' \
                         'topic_introduction, ' \
                         'author_name, ' \
                         'author_id, ' \
                         'article_time, ' \
                         'article_link, ' \
                         'article_id, ' \
                         'article_mid, ' \
                         'article_show_link, ' \
                         'article_comment_link, ' \
                         'article_longText_link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(
                insert_sql,
                (
                    # 通过uuid库获取唯一ID
                    uuid.uuid1().hex,
                    item["topic_id"],
                    item["topic_name"],
                    item["topic_introduction"],
                    item["author_name"],
                    item["author_id"],
                    item["article_time"],
                    item["article_link"],
                    item["article_id"],
                    item["article_mid"],
                    item["article_show_link"],
                    item["article_comment_link"],
                    item["article_longText_link"]
                )
            )
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
            print("数据已保存到mysql_topic_article")
        return item  # 返回item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

""" 持久化详细博文信息 """
class SaveToMysqlDB_ArticleDetailItem_Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='weibo_scrapy_data',  # 数据库名
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.conn.cursor()
        print("数据库连接成功，准备写入article_detail")

    def process_item(self, item, spider):
        if isinstance(item, Article_Detail_Item):  # 判断item是否为Article_Detail_Item类型
            # print("Article_Detail_Item: ",item)
            # sql语句，向 article_detail 表中插入数据
            insert_sql = 'insert into article_detail(' \
                         'id, ' \
                         'article_id, ' \
                         'article_content, ' \
                         'author_name, ' \
                         'article_time, ' \
                         'num_forward, ' \
                         'num_comment, ' \
                         'num_like) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(
                insert_sql,
                (
                    # 通过uuid库获取唯一ID
                    uuid.uuid1().hex,
                    item["article_id"],
                    item["article_content"],
                    item["author_name"],
                    item["article_time"],
                    item["num_forward"],
                    item["num_comment"],
                    item["num_like"]
                )
            )
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
            print("数据已保存到mysql_article_detail")
        return item  # 返回item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


""" 持久化每个博文的评论信息 """
class SaveToMysqlDB_ArticleCommentItem_Pipeline(object):
    def __init__(self):
        # self.count = 0
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='weibo_scrapy_data',  # 数据库名
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.conn.cursor()
        print("数据库连接成功，准备写入article_comment")

    def process_item(self, item, spider):
        # # 此if用来获取评论的xhr请求链接，并解析出count的值
        # if isinstance(item, Topic_Article_Item):
        #     comment_url = item["article_comment_link"]
        #     self.count = int(comment_url.split("&")[4].split("=")[1])
        # 判断item是否为Article_Detail_Item类型，从该类型中获取 comment_data , 进而解析处评论
        if isinstance(item, Article_Detail_Item):
            article_id = item["article_id"]
            count = len(item["comment_data"])
            for i in range(0, count-1):        # 有时出现越界错误
                comment_data = item["comment_data"][i]
                # sql语句，向 topic_article 表中插入数据
                insert_sql = 'insert into article_comment(' \
                             'id, ' \
                             'article_id, ' \
                             'comment_id, ' \
                             'comment_time, ' \
                             'comment_content, ' \
                             'comment_author_id, ' \
                             'comment_author_name, ' \
                             'comment_province) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                self.cursor.execute(
                    insert_sql,
                    (
                        # 通过uuid库获取唯一ID
                        uuid.uuid1().hex,
                        article_id,
                        comment_data["id"],
                        comment_data["created_at"],
                        comment_data["text"],
                        comment_data["user"]["id"],
                        comment_data["user"]["name"],
                        comment_data["source"]      # 有时出现keyError
                    )
                )
                # 提交，不进行提交无法保存到数据库
                self.conn.commit()
                print("数据已保存到mysql_article_comment")
        return item  # 返回item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

