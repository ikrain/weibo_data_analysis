import time
import uuid

import pymysql
import re

# 对 system_week_rank 表进行数据清洗和分析
# 对 话题创建时间 进行处理，只保留年月日，写入到新的数据表中———system_topic_time（一）
# 写入数据前需要先清空表中的数据
# 5月14日更新
class analysis_topic_time:
    # 链接数据库
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

    def change_time(self):
        delete_sql = 'delete from system_topic_time'
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("正在清空数据库...")
        self.conn.commit()
        select_sql = 'select topic_name, topic_time from system_week_rank'
        insert_sql = 'insert into system_topic_time' \
                     '(id, topic_name, topic_time)' \
                     'values ' \
                     '(%s, %s, %s)'
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        print("正在将过滤好的数据写入数据库...")
        for item in result:
            time = item[1].split(" ")[0]
            self.cursor.execute(
                insert_sql,
                (
                    uuid.uuid1().hex,
                    item[0],
                    time
                )
            )
            self.conn.commit()

    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

# 从数据表 article_detail 中获取格式为 2022-05-11 的文章评论时间数据，写入到 system_article_time
# 5月14日更新
class analysis_article_time:
    # 链接数据库
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

    def change_time(self):
        delete_sql = 'delete from system_article_time'
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("正在清空数据库...")
        self.conn.commit()
        select_sql = 'select article_id, article_time from article_detail'
        insert_sql = 'insert into system_article_time' \
                     '(id, article_id, article_time)' \
                     'values ' \
                     '(%s, %s, %s)'
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        print("正在将过滤好的数据写入数据库...")
        for item in result:
            time1 = self.world_to_china(item[1])
            time = time1.split(" ")[0]
            self.cursor.execute(
                insert_sql,
                (
                    uuid.uuid1().hex,
                    item[0],
                    time
                )
            )
            self.conn.commit()

    def world_to_china(self, str):
        # str = "Tue May 10 16:21:30 +0800 2022"
        struct_time = time.strptime(str, '%a %b %d %H:%M:%S %z %Y')
        return time.strftime("%Y-%m-%d %H:%M:%S", struct_time)

    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

# 从数据表 system_article_comment 中获取格式为 2022-05-11 的文章评论时间数据，写入到 system_comment_time
# 跟随 system_artile_time 仅分析一次
# 5月13日更新
class analysis_comment_time:
    # 链接数据库
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

    def change_time(self):
        delete_sql = 'delete from system_comment_time'
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("正在清空数据库...")
        self.conn.commit()
        select_sql = 'select topic_id, article_id, comment_time from system_article_comment'
        insert_sql = 'insert into system_comment_time' \
                     '(id, topic_id, article_id, comment_time)' \
                     'values ' \
                     '(%s, %s, %s, %s)'
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        print("正在将过滤好的数据写入数据库...")
        for item in result:
            time = item[2].split(" ")[0]
            self.cursor.execute(
                insert_sql,
                (
                    uuid.uuid1().hex,
                    item[0],
                    item[1],
                    time
                )
            )
            self.conn.commit()

    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()



if __name__ == '__main__':
    art = analysis_article_time()
    art.change_time()
