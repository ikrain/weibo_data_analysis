import json, simplejson

# a = {
#     "data":[
#         {"key": "aaa", "value": 111},
#         {"key": "bbb", "value": 222},
#         {"key": "ccc", "value": 333, "user":{"id":123}}
#
#     ]
# }
#
# print(a["data"][2]["user"]["id"])



# url = "https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4765331064619517&is_show_bulletin=2&is_mix=0&count=10&uid=2803301701"
#
# count= url.split("&")[4].split("=")[1]
#
# print(count)


# topic_detail_url = 'https://m.s.weibo.com/ajax_topic/detail?q=%23' + '五一假期出游人次减少30.2%' + '%23'
# topic_trend_url = 'https://m.s.weibo.com/ajax_topic/trend?q=%23' + '五一假期出游人次减少30.2%' + '%23&time=24h'
#
#
# print(topic_trend_url)
# print(topic_detail_url)