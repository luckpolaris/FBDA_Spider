import scrapy


class PeertopeerlendSpider(scrapy.Spider):
    name = 'peerToPeerLend'
    allowed_domains = ['www.renrendai.com']
    start_urls = ['http://www.renrendai.com/']

    def parse(self, response):
        pass
