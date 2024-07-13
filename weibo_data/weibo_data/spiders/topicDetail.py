import requests
import scrapy
import json
import uuid
import datetime
import pymysql

"""
    该爬虫类用于更新每个话题详情的 阅读趋势、原创趋势、讨论趋势
"""

from ..items import *

class TopicDetailSpider(scrapy.Spider):
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

    name = 'topicDetail'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']
    # 带拆分cookie
    temp = 'SINAGLOBAL=3949475012053.3115.1650875990719; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWpCS8o43o8CLW_5N2OwWXP5JpX5KMhUgL.FoqpS0eNSh-0e0q2dJLoI05LxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1KMLB-9kBcnt; ALF=1683812102; SSOLoginState=1652276102; SCF=AhFy2WfeeOgO66VfP4ikeOkGlWM3FLwdVj3tins5970CoVWT7yKOsO--KINalqQ53YjkG2WC2hFJPiG5U2NBsfs.; SUB=_2A25Pf8vZDeRhGeBP7FEW9CvPyDqIHXVsDLoRrDV8PUNbmtB-LWrtkW9NRSixFTfyyUyci2bYf2RElVoepbqL8JlV; _s_tentry=login.sina.com.cn; Apache=166485131771.13022.1652276104957; ULV=1652276105003:15:12:2:166485131771.13022.1652276104957:1652163179672'
    # 拆分temp，scrapy的cookie是类似与json的形式，
    # 不像平常在requests上直接粘贴就可以用，需要转换一下格式
    cookies = {data.split("=")[0]: data.split("=")[-1] for data in temp.split("; ")}
    headers = {
        "cookie": "SINAGLOBAL=3949475012053.3115.1650875990719; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWpCS8o43o8CLW_5N2OwWXP5JpX5KMhUgL.FoqpS0eNSh-0e0q2dJLoI05LxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1KMLB-9kBcnt; ALF=1683812102; SSOLoginState=1652276102; SCF=AhFy2WfeeOgO66VfP4ikeOkGlWM3FLwdVj3tins5970CoVWT7yKOsO--KINalqQ53YjkG2WC2hFJPiG5U2NBsfs.; SUB=_2A25Pf8vZDeRhGeBP7FEW9CvPyDqIHXVsDLoRrDV8PUNbmtB-LWrtkW9NRSixFTfyyUyci2bYf2RElVoepbqL8JlV; _s_tentry=login.sina.com.cn; Apache=166485131771.13022.1652276104957; ULV=1652276105003:15:12:2:166485131771.13022.1652276104957:1652163179672",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    # 重写 start_requests 方法，添加 cookie
    def start_requests(self):
        # url = self.start_urls[0]
        temp = 'SINAGLOBAL=3949475012053.3115.1650875990719; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWpCS8o43o8CLW_5N2OwWXP5JpX5KMhUgL.FoqpS0eNSh-0e0q2dJLoI05LxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1KMLB-9kBcnt; ALF=1683812102; SSOLoginState=1652276102; SCF=AhFy2WfeeOgO66VfP4ikeOkGlWM3FLwdVj3tins5970CoVWT7yKOsO--KINalqQ53YjkG2WC2hFJPiG5U2NBsfs.; SUB=_2A25Pf8vZDeRhGeBP7FEW9CvPyDqIHXVsDLoRrDV8PUNbmtB-LWrtkW9NRSixFTfyyUyci2bYf2RElVoepbqL8JlV; _s_tentry=login.sina.com.cn; Apache=166485131771.13022.1652276104957; ULV=1652276105003:15:12:2:166485131771.13022.1652276104957:1652163179672'
        # 拆分temp，scrapy的cookie是类似与json的形式，
        # 不像平常在requests上直接粘贴就可以用，需要转换一下格式
        cookies = {data.split("=")[0]: data.split("=")[-1]for data in temp.split("; ")}

        select_sql = 'select topic_id, topic_name from topic_detail'
        self.cursor.execute(select_sql)
        results = self.cursor.fetchall()
        for item in results:
            url = 'https://m.s.weibo.com/ajax_topic/trend?q=%23' + item[1] + '%23&time=24h'
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={'topic_id': item[0]},
                cookies=cookies
            )

    def parse(self, response):
        updateTDI = Update_Topic_Detail_Item()
        topic_id = response.meta["topic_id"]
        topic_trend_json_data = response.json()["data"]
        updateTDI["topic_id"] = topic_id
        updateTDI["topic_read_trend"] = str(topic_trend_json_data["read"])
        updateTDI["topic_talk_trend"] = str(topic_trend_json_data["me"])
        updateTDI["topic_original_trend"] = str(topic_trend_json_data["ori"])
        yield updateTDI


    def close_spider(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
