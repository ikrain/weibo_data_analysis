# Scrapy settings for weibo_data project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import weibo_data.pipelines

BOT_NAME = 'weibo_data'

SPIDER_MODULES = ['weibo_data.spiders']
NEWSPIDER_MODULE = 'weibo_data.spiders'

# 设置日志的显示，只显示error和warning
LOG_LEVEL = 'WARNING'

# 设置本机Mysql数据库的相关配置，便于将数据写入数据库中
# 主机ip地址
HOST = '127.0.0.1'
# 端口号 ---------类型为整数！！！----------
PORT = 3306
# 用户名
USER = 'root'
# 密码
PASSWD = '123456'
# 需要存入的数据库
DB = 'spider01'
# 指定字符集，注意uft-8中的‘-’，识别不了！！
CHARACTER = 'utf8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo_data (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weibo_data.middlewares.WeiboDataSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'weibo_data.middlewares.WeiboDataDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'weibo_data.pipelines.SaveToMysqlDB_HotTopicItem_Pipeline': 300,
    'weibo_data.pipelines.SaveToMysqlDB_TopicArticleItem_Pipeline': 301,
    'weibo_data.pipelines.SaveToMysqlDB_ArticleDetailItem_Pipeline': 302,
    'weibo_data.pipelines.SaveToMysqlDB_ArticleCommentItem_Pipeline': 303,
    'weibo_data.pipelines.SaveToMysqlDB_TopicDetailItem_Pipeline': 304,
    'weibo_data.pipelines.Update_TopicDetailItem_Pipeline': 305,
    'weibo_data.pipelines.Update_TopicReadNum_Pipeline': 306
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'