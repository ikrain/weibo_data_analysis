# import requests
# import csv
# import re
#
# headers = {
#     "cookie": "SINAGLOBAL=3949475012053.3115.1650875990719; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWpCS8o43o8CLW_5N2OwWXP5JpX5KMhUgL.FoqpS0eNSh-0e0q2dJLoI05LxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1K.L1hnLxK.L1KMLB-9kBcnt; UOR=,,login.sina.com.cn; ALF=1683246627; SSOLoginState=1651710627; SCF=AhFy2WfeeOgO66VfP4ikeOkGlWM3FLwdVj3tins5970Cciwm_WVlXZJJtRMgoYsriAEegjfnVFjW4LXwj5vbFwo.; SUB=_2A25Pd2r2DeRhGeBP7FEW9CvPyDqIHXVsBds-rDV8PUNbmtAKLVrWkW9NRSixFRlz3yKZhJGBqhFEhvXnS04UF7K3; _s_tentry=login.sina.com.cn; Apache=370020207036.15027.1651710630413; ULV=1651710630444:11:8:8:370020207036.15027.1651710630413:1651625189308",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
# }
#
# def get_data():
#     # 定义数据类型
#     # - 作者
#     # - 发布时间
#     # - 微博正文
#     # - 转发数
#     # - 评论数
#     # - 点赞数
#     item_all_detail = {}
#     param = {}
#     with open('D:\Program\Pycharm\weibo_data\weibo_detail.csv', 'r') as f:
#         reader = csv.DictReader(f)
#         for line in reader:
#             # 获取列名为 article_show_link 的所有值
#             article_show_link = line.pop("article_show_link")
#             article_comment_link = line.pop("article_comment_link")
#             article_longText_link = line.pop("article_longText_link")
#             # print(article_show_link)
#             try:
#                 # 发送xhr请求，获取服务器相应数据，json格式
#                 respnose_show = requests.get(article_show_link, headers=headers)
#                 respnose_comment = requests.get(article_comment_link, headers=headers)
#                 # respnose_longText = requests.get(article_longText_link, headers=headers, params=param)
#
#                 # print(respnose_show.json())
#                 # print(respnose_comment.json())
#                 # print(respnose_longText.json())
#                 comment_json_data = respnose_comment.json()
#                 # longText_json_data = respnose_longText.json()
#
#
#
#                 # - 作者、发布时间、微博正文、转发数、评论数、点赞数
#                 if respnose_show.status_code == 200:
#                     show_json_data = respnose_show.json()
#                     # item_all_detail["author_name"] = show_json_data["user"]["screen_name"]
#                     # item_all_detail["article_time"] = show_json_data["created_at"]
#                     # item_all_detail["num_forward"] = show_json_data["reposts_count"]
#                     # item_all_detail["num_comment"] = show_json_data["comments_count"]
#                     # item_all_detail["num_like"] = show_json_data["attitudes_count"]
#                     # if (show_json_data['isLongText']):
#                     #     pass
#                     #     # item_all_detail["article_content"] = longText_json_data["data"]["longTextContent"]
#                     # else:
#                     #     item_all_detail["article_content"] = show_json_data["text_raw"]
#                     return show_json_data
#             except requests.ConnectionError as e:
#                 print("Error", e.args)
#
# def get_oneData():
#     try:
#         # 发送xhr请求，获取服务器相应数据，json格式
#         # respnose_longText = requests.get("https://m.s.weibo.com/ajax_topic/detail?q=%23五一假期出游人次减少30.2%%23", headers=headers)
#         # respnose_longText = requests.get("https://m.s.weibo.com/ajax_topic/trend?q=%23五一假期出游人次减少30.2%%23&time=24h", headers=headers)
#         respnose_longText = requests.get("https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4765759630478676&is_show_bulletin=2&is_mix=0&count=10&uid=1926909715", headers=headers)
#         print("respnose_longText:",respnose_longText.text)
#         # - 作者、发布时间、微博正文、转发数、评论数、点赞数
#         if respnose_longText.status_code == 200:
#             longText_json_data = respnose_longText.json()["data"]
#             # print("data:",longText_json_data)
#             # print("read: ",longText_json_data["read"])
#             # print("read: ",type(str(longText_json_data["read"])))
#             # print("me: ",type(longText_json_data["me"]))
#             # print("ori: ",type(longText_json_data["ori"]))
#             # return longText_json_data
#             print(len(longText_json_data))
#     except requests.ConnectionError as e:
#         print("Error", e.args)
#
# def cleanData():
#     text = '#哈哈哈#'
#     print(text.replace('#',''))
#
# if __name__ == '__main__':
#    get_oneData()
