# -*- coding: utf-8 -*-
import scrapy


class WuhanmoviespiderSpider(scrapy.Spider):
    name = "wuHanMovieSpider"
    allowed_domains = ["jycinema.com"]
    start_urls = ['http://jycinema.com/']

    def parse(self, response):
        pass
