# -*- coding: utf-8 -*-

import scrapy
from bdbk.items import BdbkItem

class BDBKSpider(scrapy.Spider):
    name = "bdbk"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        # "http://baike.baidu.com/item/苹果/5670",
        "http://baike.baidu.com/item/橘子/71287?sefr=cr",
        # "http://baike.baidu.com/item/提子/53914?sefr=cr"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # for sel in response.xpath("//div[@class='lemma-summary']/div[@class='para']"):
        flag = False 
        g_content = ''
        entity = BdbkItem()
        for sel in response.xpath("//div[@class='main-content']//div"):
            title = sel.xpath("h2/text()").extract()
            desc = ''
            for item in title:
                desc += item.strip('\n')
            if len(desc) > 0:
                if flag:
                    entity['content'] = g_content
                    if len(g_content) > 1:
                        yield entity
                flag = True
                entity = BdbkItem()
                entity['section'] = desc
                print 'title: ' + desc
                g_content = ''

            content = sel.xpath("text()|a[@class!='edit-icon j-edit-link']/text()|b/text()|i/text()").extract()
            # print title
            desc = ''
            for item in content:
                desc += item.strip('\n')
            g_content += desc
        # yield entity

            # link = sel.xpath('a/@href').extract()
            # desc = sel.xpath('text()').extract()
            # print desc
            # for gg in sel.xpath("*"):
            #     info = gg.xpath('text()').extract()
            #     for xx in info:
            #         print xx
