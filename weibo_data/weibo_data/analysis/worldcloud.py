import jieba
import wordcloud
import pymysql

class Make_Week_WorldCloud:
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

    def make_text(self):
        # 清空txt文本中的所有数据
        open("worldcloud.txt", 'w').close()
        select_sql = 'select topic_name from system_week_rank'
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        topic_file = open('worldcloud.txt', mode='a+',encoding="utf-8")
        for item in result:
            topic_file.write(item[0])
            # print(item)
        topic_file.close()

    def make_worldcloud(self):
        font_path = "F:\\simfang.ttf"
        f = open("worldcloud.txt", "r", encoding="utf-8")
        t = f.read()
        f.close()
        ls = jieba.lcut(t)
        txt = " ".join(ls)
        w = wordcloud.WordCloud(
            width=1000,
            height=370,
            background_color="white",
            font_path=font_path)
        w.generate(txt)
        # w.to_file("topic_week.png")
        w.to_file(r"D:\Program\VSCode\vue-admin-template-master\vue-admin-template-master\src\assets\topic_week.png")

    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    mww = Make_Week_WorldCloud()
    mww.make_text()
    mww.make_worldcloud()