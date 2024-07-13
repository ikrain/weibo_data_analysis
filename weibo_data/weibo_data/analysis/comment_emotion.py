import time
import uuid

from snownlp import SnowNLP
import pymysql
import re
from bs4 import BeautifulSoup

# 分析 微博博文的正文，对其进行数据清洗、过滤
# 根据博文的点赞数，仅从 article_detail 表中获取并分析了热度前四百的博文，
# 分析完后写入 system_article_search（四） 表中
class analysisArticleContentEmotion:
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

    # 利用正则表达式进行数据的清洗
    def filterContent(self, content):
        text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", content)  # 去除正文中的@和回复/转发中的用户名
        text = re.sub(r"\[\S+\]", "", text)  # 去除表情符号
        text = re.sub(r"#\S+#", "", text)  # 保留话题内容
        URL_REGEX = re.compile(
            r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
            re.IGNORECASE)
        text = re.sub(URL_REGEX, "", text)  # 去除网址
        text = re.sub(r'[’!"#$%&\'()*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！\[\\\]^_`{|}~]+', "", text)  # 删除特殊字符
        text = text.replace("转发微博", "")  # 去除无意义的词语
        text = re.sub(r"\s+", " ", text)  # 合并正文中过多的空格
        return text.strip()

    # 利用 SnowNLP 模型获取情感值
    def getEmotionValue(self, article_content):
        s = SnowNLP(article_content)
        sentiments = s.sentiments
        return sentiments

    # 查询数据表，进行数据的过滤与分析
    # 根据博文的点赞数，仅从 article_detail 表中获取并分析了热度前四百的博文，
    # 分析完后写入 system_article_search（四） 表中
    def do_analysis(self):
        delete_sql = 'delete from system_article_search'
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("正在清空数据库...")
        select_sql = 'select article_id, author_name, article_content, ' \
                     'article_time, num_like, num_forward, num_comment ' \
                     'from article_detail order by num_like desc limit 400;'
        insert_sql = "insert into system_article_search " \
                     "(id, " \
                     "article_id, " \
                     "author_name, " \
                     "article_content, " \
                     "article_time, " \
                     "article_emotion, " \
                     "emotion_state, " \
                     "article_hot_value) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        print("正在将处理好的数据写入数据库...")
        for item in result:
            article_content = self.filterContent(item[2])
            if article_content != None and article_content != "":
                # 基于某种特定的分配，根据转发、点赞、评论数计算 博文的 热度值
                hot_value = int(item[4])*0.3 + int(item[5])*0.4 + int(item[6])*0.3
                article_hot_value = hot_value
                article_time = self.test(item[3])
                emotion = self.getEmotionValue(article_content)-0.5
                article_emotion = str(round(emotion, 2))
                if emotion > 0.1:
                    emotion_state = '积极'
                elif emotion < -0.1:
                    emotion_state = '消极'
                else:
                    emotion_state = '中立'
                self.cursor.execute(
                    insert_sql,
                    (
                        uuid.uuid1().hex,
                        item[0],
                        item[1],
                        article_content,
                        article_time,
                        article_emotion,
                        emotion_state,
                        article_hot_value
                    )
                )
                self.conn.commit()

    # 关闭数据库
    def __del__(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

    # 将 包含时区的时间格式 转为 正常格式
    def test(self, str):
        # str = "Tue May 10 16:21:30 +0800 2022"
        struct_time = time.strptime(str, '%a %b %d %H:%M:%S %z %Y')
        return time.strftime("%Y-%m-%d %H:%M:%S", struct_time)


# 对 每个话题下的 所有博文的 微博评论 进行清洗、过滤、数据分析
# 仅分析一次
class analysisTopicArticleComment:
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
        print("数据库已连接")

    # 利用正则表达式进行数据的清洗
    def filterContent(self, content):
        # 先使用 BeautifulSoup 去除评论中的 表情html 标签
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text()
        text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
        text = re.sub(r"\[\S+\]", "", text)  # 去除表情符号
        text = re.sub(r"#\S+#", "", text)  # 保留话题内容
        URL_REGEX = re.compile(
            r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
            re.IGNORECASE)
        text = re.sub(URL_REGEX, "", text)  # 去除网址
        text = re.sub(r'[’!"#$%&\'()*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！\[\\\]^_`{|}~]+', "", text)  # 删除特殊字符
        text = text.replace("img", "")  # 去除无意义的词语
        text = text.replace("alt", "")  # 去除无意义的词语
        text = text.replace("title", "")  # 去除无意义的词语
        text = text.replace("src", "")  # 去除无意义的词语 a href t
        text = text.replace(" a href t", "")  # 去除无意义的词语
        text = re.sub(r"\s+", " ", text)  # 合并正文中过多的空格
        return text.strip()

    # 利用 SnowNLP 模型获取情感值
    def getEmotionValue(self, article_content):
        s = SnowNLP(article_content)
        sentiments = s.sentiments
        return sentiments

    # 将计算后的结果保存到数据库
    def save_to_mysql(self):
        select_sql = 'select ' \
                     'a.topic_id,' \
                     'a.topic_name,' \
                     'c.article_id,' \
                     'c.comment_time,' \
                     'c.comment_content,' \
                     'c.comment_author_name ' \
                     'from article_comment c join topic_article a on c.article_id=a.article_id'

        insert_sql = "insert into system_article_comment " \
                     "(id, " \
                     "topic_id," \
                     "topic_name," \
                     "article_id," \
                     "comment_time," \
                     "comment_content," \
                     "comment_author_name," \
                     "comment_emotion," \
                     "emotion_state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        for item in result:
            # 使用正则表达式、BeautifulSoup等方式对数据进行清洗、过滤
            article_comment = self.filterContent(item[4])
            # print(item)
            if article_comment != None and article_comment != "":
                article_time = self.test(item[3])
                emotion = self.getEmotionValue(article_comment) - 0.5
                comment_emotion = str(round(emotion, 2))
                if emotion > 0.1:
                    emotion_state = '积极'
                elif emotion < -0.1:
                    emotion_state = '消极'
                else:
                    emotion_state = '中立'
                self.cursor.execute(
                    insert_sql,
                    (
                        uuid.uuid1().hex,
                        item[0],
                        item[1],
                        item[2],
                        article_time,
                        article_comment,
                        item[5],
                        comment_emotion,
                        emotion_state
                    )
                )
                self.conn.commit()

    # 关闭数据库
    def __del__(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
        print("数据库已关闭")

    # 将 包含时区的时间格式 转为 正常格式
    def test(self, str):
        # str = "Tue May 10 16:21:30 +0800 2022"
        struct_time = time.strptime(str, '%a %b %d %H:%M:%S %z %Y')
        return time.strftime("%Y-%m-%d %H:%M:%S", struct_time)

if __name__ == '__main__':
    analysisArticleContentEmotion().do_analysis()
    # analysisTopicArticleComment().save_to_mysql()