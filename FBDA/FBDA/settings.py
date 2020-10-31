# -*- coding: utf-8 -*-

# Scrapy settings for FBDA project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'FBDA'

SPIDER_MODULES = ['FBDA.spiders']
NEWSPIDER_MODULE = 'FBDA.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh - CN, zh; q = 0.9',
    'Connection': 'keep - alive',
    'Host': 'www.renrendai.com',
    'Referer': 'https://www.renrendai.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'rrdid=97a7e787-9ddf-4182-9622-a9d37020b0e4; __jsluid_s=e1aa41528c5cb79af05fde8530900452; gr_user_id=3a6c3add-ad06-4cba-847c-1155021cda43; grwng_uid=82cb1941-ce90-4824-9a3e-56c934763ebd; _ga=GA1.2.1517765865.1603711246; registerSource=web_top; _gid=GA1.2.1522634968.1603933709; loginMethod=sms; renrendaiUsername=17306445213; jforumUserInfo=TEZxUXSaBc%2By6bLjOd0IBRY7Q9PXR0j%2FFJN6FcAwPsE%3D%0A; Qs_lvt_181814=1603933708%2C1603966589%2C1603969624%2C1604020163%2C1604023550; Hm_lvt_a00f46563afb7c779eef47b5de48fcde=1603969625,1604020164,1604023550,1604036428; activeTimestamp=19320192; IS_MOBLIE_IDPASS=true-false; we_token=WG1EQnJqMVpkUmhjU3BiRUdoT3MzelRYd3FyYVE3eU06MTkzMjAxOTI6MjQ3MmMyOTNjYTBmOGRmOWIyMzNmMGQ4NGRlMDZiZWYwYjA5YTcwOQ%3D%3D; we_sid=s%3ADYcBhhpE_0cL573YId4qD30f9Ve0xQB_.M1A6R3ht5s0WKSFNgTR8DlCspKbzAZCKszuDsaHJV7Q; 9199126ed94d770d_gr_last_sent_sid_with_cs1=02e26ecb-642e-4b73-a52c-9951a3d0fbf4; 9199126ed94d770d_gr_last_sent_cs1=19320192; 9199126ed94d770d_gr_session_id=02e26ecb-642e-4b73-a52c-9951a3d0fbf4; 9199126ed94d770d_gr_session_id_02e26ecb-642e-4b73-a52c-9951a3d0fbf4=true; JSESSIONID=3A62E573FB77F1B2F2D7D896F6C6FC77; Qs_pv_181814=852484596927216500%2C2295503303876376600%2C4342495844457035300%2C1031981478543316100%2C3177497334737962500; 9199126ed94d770d_gr_cs1=19320192; Hm_lpvt_a00f46563afb7c779eef47b5de48fcde=1604038741; mediav=%7B%22eid%22%3A%22301358%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A1%2C%22_refnf%22%3A1%7D'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'FBDA.middlewares.FbdaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'FBDA.middlewares.FbdaDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'FBDA.pipelines.FbdaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
