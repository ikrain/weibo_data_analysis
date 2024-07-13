import requests
import scrapy
import json
import uuid
import datetime

from ..items import *

# - 热门话题
# - 热门话题对应博文链接
# - 话题热门指数
# - 话题排行
# - 话题下所有博文（后期在数据库中存储时，使用一对多的关系，在博文数据库中存储其热点话题的主键）

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']
    # 带拆分cookie
    temp = 'SINAGLOBAL=3949475012053.3115.1650875990719; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWpCS8o43o8CLW_5N2OwWXP5JpX5KMhUgL.FoqpS0eNSh-0e0q2dJLoI05LxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1KMLB-9kBcnt; ALF=1683986951; SSOLoginState=1652450952; SCF=AhFy2WfeeOgO66VfP4ikeOkGlWM3FLwdVj3tins5970ChPhE54UBO9l1Lgk412S3Oe3AHbo4N-f9MW0dJnIB_-U.; SUB=_2A25PehbbDeRhGeBP7FEW9CvPyDqIHXVsDg8TrDV8PUNbmtB-LRH7kW9NRSixFYZj0zoHqCa_mE7pe_2lYxgMBZNG; _s_tentry=login.sina.com.cn; Apache=5008303241120.145.1652450956374; ULV=1652450956422:18:15:5:5008303241120.145.1652450956374:1652315498961; UOR=,,localhost:8081; XSRF-TOKEN=Bb8ohB8NnCZmeM-q_DnGfslD; WBPSESS=JP9SVT7YSuuz7XmtDAcAGOqn-ctCboCQoVGL7vOxBs3Wajf1JHpVLYDSqthTLY7kXVlEK2iGLNohY28T-3J_5hGdBnuR1d-pggWjCx3Mf_EB-W5bVScGHDLnXXYncCN7YHueboPA3m9649iBy5sYBg=='
    # 拆分temp，scrapy的cookie是类似与json的形式，
    # 不像平常在requests上直接粘贴就可以用，需要转换一下格式
    cookies = {data.split("=")[0]: data.split("=")[-1] for data in temp.split("; ")}

    headers = {
        "cookie": "SINAGLOBAL=3949475012053.3115.1650875990719; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWpCS8o43o8CLW_5N2OwWXP5JpX5KMhUgL.FoqpS0eNSh-0e0q2dJLoI05LxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1KMLB-9kBcnt; ALF=1683986951; SSOLoginState=1652450952; SCF=AhFy2WfeeOgO66VfP4ikeOkGlWM3FLwdVj3tins5970ChPhE54UBO9l1Lgk412S3Oe3AHbo4N-f9MW0dJnIB_-U.; SUB=_2A25PehbbDeRhGeBP7FEW9CvPyDqIHXVsDg8TrDV8PUNbmtB-LRH7kW9NRSixFYZj0zoHqCa_mE7pe_2lYxgMBZNG; _s_tentry=login.sina.com.cn; Apache=5008303241120.145.1652450956374; ULV=1652450956422:18:15:5:5008303241120.145.1652450956374:1652315498961; UOR=,,localhost:8081; XSRF-TOKEN=Bb8ohB8NnCZmeM-q_DnGfslD; WBPSESS=JP9SVT7YSuuz7XmtDAcAGOqn-ctCboCQoVGL7vOxBs3Wajf1JHpVLYDSqthTLY7kXVlEK2iGLNohY28T-3J_5hGdBnuR1d-pggWjCx3Mf_EB-W5bVScGHDLnXXYncCN7YHueboPA3m9649iBy5sYBg==",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    # 重写 start_requests 方法，添加 cookie
    def start_requests(self):
        url = self.start_urls[0]

        temp = 'SINAGLOBAL=3949475012053.3115.1650875990719; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWpCS8o43o8CLW_5N2OwWXP5JpX5KMhUgL.FoqpS0eNSh-0e0q2dJLoI05LxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1KMLB-9kBcnt; ALF=1683986951; SSOLoginState=1652450952; SCF=AhFy2WfeeOgO66VfP4ikeOkGlWM3FLwdVj3tins5970ChPhE54UBO9l1Lgk412S3Oe3AHbo4N-f9MW0dJnIB_-U.; SUB=_2A25PehbbDeRhGeBP7FEW9CvPyDqIHXVsDg8TrDV8PUNbmtB-LRH7kW9NRSixFYZj0zoHqCa_mE7pe_2lYxgMBZNG; _s_tentry=login.sina.com.cn; Apache=5008303241120.145.1652450956374; ULV=1652450956422:18:15:5:5008303241120.145.1652450956374:1652315498961; UOR=,,localhost:8081; XSRF-TOKEN=Bb8ohB8NnCZmeM-q_DnGfslD; WBPSESS=JP9SVT7YSuuz7XmtDAcAGOqn-ctCboCQoVGL7vOxBs3Wajf1JHpVLYDSqthTLY7kXVlEK2iGLNohY28T-3J_5hGdBnuR1d-pggWjCx3Mf_EB-W5bVScGHDLnXXYncCN7YHueboPA3m9649iBy5sYBg=='

        # 拆分temp，scrapy的cookie是类似与json的形式，
        # 不像平常在requests上直接粘贴就可以用，需要转换一下格式
        cookies = {data.split("=")[0]: data.split("=")[-1]for data in temp.split("; ")}

        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies
        )

        # yield scrapy.Request(
        #     url='https://weibo.com/ajax/statuses/show?id=Lr7Bl5by6',
        #     callback=self.Article_Detail_Parse,
        #     cookies=cookies
        # )

    def parse(self, response):

        li_list = response.xpath("//div[@class='data']//tr")

        # 获取热榜话题
        for li in li_list:
            # 1. 微博热榜话题
            hotTopicItem = Hot_Topic_Item()
            hotTopicItem["topic_name"] = li.xpath(".//a/text()").extract_first()
            hotTopicItem["topic_rank"] = li.xpath(".//td[@class='td-01 ranktop']/text()").extract_first()
            hotTopicItem["topic_num"] = li.xpath(".//span/text()").extract_first()
            # 获取到的链接是相对路径链接，使用response.urljoin()进行拼接
            hotTopicItem["topic_link"] = response.urljoin(li.xpath(".//a/@href").extract_first())
            # 获取爬取微博数据时的时间
            hotTopicItem["topic_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 生成热门话题ID
            topic_id_public = uuid.uuid1().hex
            hotTopicItem["topic_id"] = topic_id_public

            # print(hotTopicItem)
            print("hotTopicItem传入管道...")
            """ 将 hotTopicItem 传给管道用于保存到数据库 """
            yield hotTopicItem

            # 根据每个热榜话题的链接，发送请求获取每个热榜下的简要博文信息
            url = response.urljoin(li.xpath(".//a/@href").extract_first())
            flag = "javascript:void(0);" in url
            # 布尔值去反
            if bool(1-flag):
                yield scrapy.Request(
                    url=url,
                    callback=self.Topic_Article_Pares,
                    meta={'topic_id_public': topic_id_public},
                    cookies=self.cookies
                )

    # 对 每个热榜话题下的博文、热门话题详情 进行数据获取与解析
    def Topic_Article_Pares(self, response):
        # 获取热榜话题下，每个博文的简要信息
        mid_list = response.xpath("//div[@action-type='feed_list_item']")

        # 1. 热点话题名称
        topic_name = str(response.xpath("//*[@id='pl_topic_header']/div[1]/div[2]/div/div[1]/h1/a/text()").extract_first()).replace('#','')
        # 2. 话题导语
        topic_introduction = response.xpath("//*[@id='pl_feedlist_index']/div[2]/div[1]/p/text()").extract_first()
        # 2.0 话题ID（其中参数来自parse回调函数）
        topic_id = response.meta["topic_id_public"]

        # 声明item数据类型，热门话题详情信息（分类、趋势）
        topicDetailItem = Topic_Detail_Item()

        # 2.1 获取热门话题详情链接，向 detail 发送 xhr 请求，获取json数据
        topic_detail_url = 'https://m.s.weibo.com/ajax_topic/detail?q=%23'+ topic_name + '%23'
        respnose_topic_detail = requests.get(url=topic_detail_url, headers=self.headers)
        topic_detail_json_data = respnose_topic_detail.json()["data"]
        # 封装数据
        topicDetailItem["topic_id"] = response.meta["topic_id_public"]
        topicDetailItem["topic_name"] = topic_detail_json_data["baseInfo"]["topic_ori"]
        topicDetailItem["topic_category"] = topic_detail_json_data["baseInfo"]["object"]["category_str"]
        topicDetailItem["topic_introduction"] = topic_detail_json_data["baseInfo"]["object"]["summary"]
        topicDetailItem["topic_host"] = topic_detail_json_data["baseInfo"]["claim_info"]["name"]
        topicDetailItem["topic_location"] = topic_detail_json_data["baseInfo"]["claim_info"]["location"]
        # 此处获取了
        # "r": {
        #     "val": 1.6,
        #     "unit": "亿"
        # }
        # 类似的数据格式，因此需要拼接
        topicDetailItem["topic_read_num"] = str(topic_detail_json_data["baseData"]["r"]["val"]) + topic_detail_json_data["baseData"]["r"]["unit"]
        topicDetailItem["topic_talk_num"] = str(topic_detail_json_data["baseData"]["m"]["val"]) + topic_detail_json_data["baseData"]["m"]["unit"]
        topicDetailItem["topic_original_num"] = str(topic_detail_json_data["baseData"]["ori_uv"]["val"]) + topic_detail_json_data["baseData"]["ori_uv"]["unit"]

        # 2.2 获取热门话题详情链接，向 detail 发送 xhr 请求，获取json数据
        topic_trend_url = 'https://m.s.weibo.com/ajax_topic/trend?q=%23' + topic_name + '%23&time=24h'
        respnose_topic_trend = requests.get(url=topic_trend_url, headers=self.headers)
        topic_trend_json_data = respnose_topic_trend.json()["data"]
        # 由于获去到的 “阅读趋势、讨论趋势、原创人数趋势” 均为如下格式：
        #read:  [
        #           {'time': '15:00', 'value': 0},
        #           {'time': '16:00', 'value': 0},
        #           {'time': '17:00', 'value': 0},
        #           ...
        #           {'time': '13:00', 'value': 1110},
        #           {'time': '14:00', 'value': 2220}
        #       ]
        # 因此需要转为字符串类型，用时在进行解析
        topicDetailItem["topic_read_trend"] = str(topic_trend_json_data["read"])
        topicDetailItem["topic_talk_trend"] = str(topic_trend_json_data["me"])
        topicDetailItem["topic_original_trend"] = str(topic_trend_json_data["ori"])

        print("topicDetailItem传入管道...")
        yield topicDetailItem

        # 解析话题下所有博文的简要信息
        for li in mid_list:
            # 每个话题下的简要博文信息
            topicArticleItem = Topic_Article_Item()
            # 1. 热点话题名称
            topicArticleItem["topic_name"] = topic_name
            # 2. 话题导语
            topicArticleItem["topic_introduction"] = topic_introduction
            # 2.0 话题ID（其中参数来自parse回调函数）
            topicArticleItem["topic_id"] = topic_id
            # 3. 作者昵称
            topicArticleItem["author_name"] = li.xpath(".//div[@class='card']//div[@class='content']//div[@class='info']//a/@nick-name").extract_first()
            # 5. 发文时间
            topicArticleItem["article_time"] = str(li.xpath(".//div[@class='card']//div[@class='content']//p[@class='from']/a/text()").extract_first()).strip()
            # 6. 博文正文链接
            topicArticleItem["article_link"] = li.xpath(".//div[@class='card']//div[@class='content']//p[@class='from']/a[1]/@href").extract_first()
            # 根据博文链接，分离出作者的 uid、博文的 article_id
            str_list = str(topicArticleItem["article_link"]).split('/')
            author_id = str_list[3]
            article_id = str_list[4].split('?')[0]
            # 4. 作者uid：从头像的超链接处获得
            topicArticleItem["author_id"] = author_id
            # 7. 每个博文的ID
            topicArticleItem["article_id"] = article_id
            # 8. 热搜榜对应博文的mid
            topicArticleItem["article_mid"] = li.xpath(".//@mid").extract_first()

            # 9. 获取show链接，该请求链接可获得json数据，其中包括 isLongText 属性，其标志是否为长文
            topicArticleItem["article_show_link"] = 'https://weibo.com/ajax/statuses/show?id=' + article_id
            # 10. 获取评论的请求链接
            topicArticleItem["article_comment_link"] = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=' \
                                           + topicArticleItem["article_mid"] \
                                           + '&is_show_bulletin=2&is_mix=0&count=10&uid=' \
                                           + author_id
            # 11. 获取长文链接
            topicArticleItem["article_longText_link"] = 'https://weibo.com/ajax/statuses/longtext?id=' + article_id

            print("topicArticleItem传入管道...")
            """ 将 topicArticleItem 传送给管道，用于存储到数据库 """
            yield topicArticleItem

            # 声明item数据类型，博文详情信息（同时记录某博文下所有的评论信息）
            articleDetailItem = Article_Detail_Item()

            """根据show请求链接获取数据"""
            # 微博正文、转发数、评论数、点赞数、评论
            show_url = topicArticleItem["article_show_link"]
            respnose_show = requests.get(url=show_url, headers=self.headers)
            show_json_data = respnose_show.json()
            articleDetailItem["article_id"] = article_id
            articleDetailItem["author_name"] = show_json_data["user"]["screen_name"]
            articleDetailItem["article_time"] = show_json_data["created_at"]
            articleDetailItem["num_forward"] = show_json_data["reposts_count"]
            articleDetailItem["num_comment"] = show_json_data["comments_count"]
            articleDetailItem["num_like"] = show_json_data["attitudes_count"]

            """根据longText请求链接获取数据"""
            longText_url = topicArticleItem["article_longText_link"]
            respnose_longText= requests.get(url=longText_url, headers=self.headers)
            longText_json_data = respnose_longText.json()

            # 根据 show_data中的数据属性 isLongText 判断是否为长文，进而获取微博正文
            if show_json_data['isLongText']:
                articleDetailItem["article_content"] = longText_json_data["data"]["longTextContent"].strip().replace('\u200b','')
            else:
                articleDetailItem["article_content"] = show_json_data["text_raw"].strip().replace('\u200b','')

            """根据comment请求链接获取数据"""
            comment_url = topicArticleItem["article_comment_link"]
            respnose_comment = requests.get(url=comment_url, headers=self.headers)
            comment_json_data = respnose_comment.json()

            # 直接获取某个博文下所有的评论
            articleDetailItem["comment_data"] = comment_json_data["data"]

            print("articleDetailItem传入管道...")
            """ 将 articleDetailItem 传送给管道，用于存储到数据库 """
            yield articleDetailItem

