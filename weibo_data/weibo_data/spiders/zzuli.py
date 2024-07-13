import scrapy


class ZzuliSpider(scrapy.Spider):
    name = 'zzuli'
    allowed_domains = ['info.zzuli.edu.cn']
    start_urls = ['http://info.zzuli.edu.cn/_t961/xsbg/list.htm']

    def parse(self, response):
        li_list = response.xpath("//td[@class='lists']//tr")
        base_url = "http://info.zzuli.edu.cn/"
        for li in li_list:
            item = {}
            item["title"] = li.xpath(".//a/text()").extract_first()
            item["time"] = li.xpath(".//div/text()").extract_first()

            # 此处获取的链接是相对路径链接，可以使用如下第一种方式进行拼接，也可以使用response.urljoin()
            # item["link"] = base_url + li.xpath(".//a/@href").extract_first()
            item["link"] = response.urljoin(li.xpath(".//a/@href").extract_first())
            print(item)
