# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem


class XicispiderSpider(scrapy.Spider):
    name = "xiciSpider"
    allowed_domains = ["xicidaili.com"]
    start_urls = []
    wds = ['nn','nt','wn','wt']
    pages = 20
    for type in wds:
        for i in range(1,pages+1):
            start_urls.append('http://xicidaili.com/' + type + '/' + str(i))
    # start_urls = ['http://xicidaili.com/']

    def parse(self, response):
        subSelector = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        items = []
        for sub in subSelector:
            item = GetproxyItem()
            item['ip'] = sub.xpath('.//td[2]/text()').extract()[0]
            item['port'] = sub.xpath('.//td[2]/text()').extract()[0]
            item['type'] = sub.xpath('.//td[2]/text()').extract()[0]
            item['location'] = sub.xpath('.//td[2]/text()').extract()[0]
            item['protocol'] = sub.xpath('.//td[2]/text()').extract()[0]
            item['source'] = sub.xpath('.//td[2]/text()').extract()[0]
            items.append(item)
        return items