import pymysql
import re

# 对 hot_topic 表进行数据清洗和分析
# 从中获取 话题ID、话题名称、话题热度、话题创建时间 数据，写入到新的数据表中———system_week_rank（一）
# 写入数据前需要先清空表中的数据
# 5月14日更新
class analysis_rank_topic:
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

    def count_topic_area(self):
        delete_sql = 'delete from system_week_rank'
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("正在清空数据库...")
        self.conn.commit()
        select_sql = 'select topic_id, topic_name, topic_link, topic_num, topic_time from hot_topic'
        insert_sql = 'insert into system_week_rank' \
                     '(id, topic_name, topic_link, topic_num, topic_time)' \
                     'values ' \
                     '(%s, %s, %s, %s, %s)'
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        print("正在将过滤好的数据写入数据库...")
        for item in result:
            if item[3] != None and item[3] != " ":          # 首先对从Mysql中获取到的数据进行过滤，过滤掉
                topic_num = re.split(" ", item[3])[1]       # 利用正则表达式 re ，对 热度 属性进行清洗
                topic_int_num = int(topic_num)                  # 将字符串类型转化为整型
                # print(item[0], item[1], item[2], int(topic_num), item[4])
                self.cursor.execute(
                    insert_sql,
                    (
                        item[0],
                        item[1],
                        item[2],
                        topic_int_num,
                        item[4]
                    )
                )
                self.conn.commit()

    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    art = analysis_rank_topic()
    art.count_topic_area()
