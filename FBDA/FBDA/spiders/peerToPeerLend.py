import json

import scrapy
from pip._vendor import requests
from pip._vendor.requests import RequestException


class PeertopeerlendSpider(scrapy.Spider):
    name = 'peerToPeerLend'
    allowed_domains = ['www.renrendai.com']
    base_url = 'https://www.renrendai.com/loan/list/loanList?'
    startNum = range(2)
    limit = '100'
    start_urls = [base_url + 'startNum=' + str(startNum) + '&limit=' + limit]
    count = 0

    def parse(self, response):
        pass
