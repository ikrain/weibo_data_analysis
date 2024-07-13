import pymysql
import uuid

# 中国地图，各省份用户活跃度分析
# 从数据表 article_comment 中分析统计出各省份用户活跃数，写入 system_comment_map（三） 表中
# 写入前需要先清空对应的数据库
# 5月14日更新
class analysis_comment_map:
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

    def count_comment_province(self):
        delete_sql = 'delete from system_comment_map'
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("正在清空数据库...")
        select = "select count(*) from article_comment where comment_province='来自";
        insert = "insert into system_comment_map (id, province, comment_num) VALUES (%s,%s,%s)"
        provinces = ["北京", "天津", "上海", "重庆", "新疆", "西藏", "宁夏", "内蒙古",
                     "广西", "黑龙江", "吉林", "辽宁", "河北", "山东", "江苏", "安徽",
                     "浙江", "福建", "广东", "海南", "云南", "贵州", "四川", "湖南",
                     "湖北", "河南", "山西", "陕西", "甘肃", "青海", "江西", "中国台湾", "中国香港", "中国澳门"]
        print("正在将处理好的数据写入数据库...")
        for p in provinces:
            select_sql = select + p + "'"
            self.cursor.execute(select_sql)
            results = self.cursor.fetchall()
            num = results[0][0]
            self.cursor.execute(
                insert,
                (
                    # 通过uuid库获取唯一ID
                    uuid.uuid1().hex,
                    p,
                    num
                )
            )
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()

    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

# 首页饼状图，热门话题所属领域分析
# 从指定的表中统计出每个领域不同的话题数
# 从原始数据表 topic_detail 中清洗、分析出数据 到 system_topic_area（二） 中
# 5月14日更新
class analysis_topic_area:
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
        delete_sql = 'delete from system_topic_area'
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("正在清空数据库...")
        select_sql = "select topic_category from topic_detail";
        self.cursor.execute(select_sql)
        results = self.cursor.fetchall()
        print("results: ", len(results))
        category_dic = {}
        for item in results:
            if item[0] not in category_dic:
                category_dic[item[0]] = 1
            else:
                category_dic[item[0]] = category_dic[item[0]] + 1
        insert_sql = "insert into system_topic_area (id, category, category_num) values (%s,%s,%s)"
        print("正在将处理好的数据写入数据库...")
        for key,value in category_dic.items():
            self.cursor.execute(
                insert_sql,
                (
                    # 通过uuid库获取唯一ID
                    uuid.uuid1().hex,
                    key,
                    int(value)
                )
            )
            self.conn.commit()


    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    """ 分析评论者所在省份 """
    acm = analysis_comment_map()
    acm.count_comment_province()

    """ 分析话题所属领域 """
    # ata = analysis_topic_area()
    # ata.count_topic_area()