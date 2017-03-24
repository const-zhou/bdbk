# -*- coding: utf-8 -*-

import scrapy
import json
from bdbk.items import BdbkItem, SectionItem

class BDBKSpider(scrapy.Spider):
    name = "bdbk"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://baike.baidu.com/item/苹果/5670",
        # "http://baike.baidu.com/item/橘子/71287?sefr=cr",
        # "http://baike.baidu.com/item/提子/53914?sefr=cr"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # for sel in response.xpath("//div[@class='lemma-summary']/div[@class='para']"):
        flag = False 
        g_content = ''
        entity = BdbkItem()
        sectionList = []
        sectionItem = SectionItem()
        for sel in response.xpath("//div[@class='main-content']//div"):
            title = sel.xpath("h2/text()").extract()
            desc = ''
            for item in title:
                desc += item.strip('\n')
            if len(desc) > 0:
                if flag:
                    sectionItem['content'] = g_content
                    if len(g_content) > 1:
                        sectionList.append(sectionItem)
                        # yield entity
                flag = True
                sectionItem = SectionItem()
                sectionItem['title'] = desc
                # print sel
                
                print 'title: ' + desc
                g_content = ''
                
            
            sectionItem['image_urls'] = sel.xpath("a[@class='image-link']/img/@src")
            print sectionItem['image_urls']

            content = sel.xpath("text()|a[@class!='edit-icon j-edit-link']/text()|b/text()|i/text()").extract()
            # print title
            desc = ''
            for item in content:
                desc += item.strip('\n')
            g_content += desc
        entity.section = sectionList
        for sel in response.xpath("//div[@class='main-content']"):
            name = sel.xpath("//h1/text()")[0].extract()
            desc = ''
            for item in sel.xpath("//div[@class='lemma-summary']/div[@class='para']"):
                title = item.xpath('text()|a/text()|b/text()|i/text()').extract()
                for item in title:
                    desc += item.strip('\n')
            content = desc
            entity.name = name
            entity.discription = content
            print name
            print content
        
        # print entity.convert2Diction()
        # json_str = json.dump(entity.convert2Diction())
        with open('data.json', 'w') as xxf:
            json.dump(entity.convert2Diction(), xxf)
        # yield entity

            # link = sel.xpath('a/@href').extract()
            # desc = sel.xpath('text()').extract()
            # print desc
            # for gg in sel.xpath("*"):
            #     info = gg.xpath('text()').extract()
            #     for xx in info:
            #         print xx
