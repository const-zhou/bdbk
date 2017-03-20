# -*- coding: utf-8 -*-

import scrapy

class BDBKSpider(scrapy.Spider):
    name = "bdbk"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://baike.baidu.com/item/苹果/5670",
        "http://baike.baidu.com/item/橘子/71287?sefr=cr",
        "http://baike.baidu.com/item/提子/53914?sefr=cr"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # for sel in response.xpath("//div[@class='lemma-summary']/div[@class='para']"):
        for sel in response.xpath("//div[@class='para']"):
            title = sel.xpath('text()|a/text()|b/text()|i/text()').extract()
            desc = ''
            for item in title:
                desc += item.strip('\n')
            print desc

                
            # link = sel.xpath('a/@href').extract()
            # desc = sel.xpath('text()').extract()
            # print desc
            # for gg in sel.xpath("*"):
            #     info = gg.xpath('text()').extract()
            #     for xx in info:
            #         print xx