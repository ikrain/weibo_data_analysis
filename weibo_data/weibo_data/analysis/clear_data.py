import pymysql
import re

# 清理过期数据
class clear_data:
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

    def doClear(self):
        delete_sql = 'delete from system_week_rank'
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("正在清空数据库...")
        self.conn.commit()

    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    cd = clear_data()
    cd.doClear()
