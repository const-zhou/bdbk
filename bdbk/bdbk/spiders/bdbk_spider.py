# -*- coding: utf-8 -*-

import scrapy

class BDBKSpider(scrapy.Spider):
    name = "bdbk"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://baike.baidu.com/item/苹果/5670"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath("//div[@class='lemma-summary']/div[@class='para']"):
            title = sel.xpath('a/text()').extract()
            # link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            for info in desc:
                print info
            
