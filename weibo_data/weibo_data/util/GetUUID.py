import uuid
# hex用于去除生成ID中带有的减号：“-”
# print(uuid.uuid1().hex)

# for i in range(1,10):
#     print(i)
# import datetime
#
# def getDate():
#     print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
from bs4 import BeautifulSoup

def getMap():
    arr = ['社会','财经','体育','体育','体育','体育','体育','体育']
    dic = {}
    for str in arr:
        if str not in dic:
            dic[str] = 1
        else:
            dic[str] = dic[str] + 1
    print(dic.keys)
    for key,value in dic.items():
        print(key, value)

def getText():
    str = '杀青快乐<a href="//s.weibo.com/weibo?q=%23%E9%87%8D%E7%94%9F%E4%B9%8B%E9%97%A8%23" target="_blank">期待精彩演绎早日播出<img alt="[打call]" title="[打call]" src="https://face.t.sinajs.cn/t4/appstyle/expression/ext/normal/39/moren_dacall02_org.png" />'
    soup = BeautifulSoup(str, 'html.parser')
    print(soup.get_text())

if __name__ == '__main__':
    getText();