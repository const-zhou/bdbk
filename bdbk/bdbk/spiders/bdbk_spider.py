# -*- coding: utf-8 -*-

import scrapy
import json
import urllib2
from bdbk.items import BdbkItem, SectionItem
from scrapy_splash import SplashRequest


class BDBKSpider(scrapy.Spider):
    name = "bdbk"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://baike.baidu.com/item/%E8%8B%B9%E6%9E%9C/5670",
        # "http://baike.baidu.com/item/苹果/5670",
        # "http://baike.baidu.com/item/橘子/71287?sefr=cr",
        # "http://baike.baidu.com/item/提子/53914?sefr=cr"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        # "http://baike.baidu.com/item/香蕉/150475?sefr=cr",
        # "http://baike.baidu.com/item/火龙果/240065?sefr=cr",
        # "http://baike.baidu.com/item/丑柑?sefr=cr",
        # "http://baike.baidu.com/item/梨/11871?sefr=cr"
    ]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         # url = url.decode('gbk', 'replace')
    #         # url = urllib2.quote(url.encode('utf-8', 'replace'))
    #         yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        # html = response.body
        # myimg = response.xpath('//a/img/@src').extract()
        # print myimg
        # response = html
        # print html
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
                
                # print 'title: ' + desc
                g_content = ''
                
            
            sectionItem['image_urls'] = sel.xpath("a[@class='image-link']/img/@src")
            # print sectionItem['image_urls']

            myimg = sel.xpath("img/@src").extract()
            if len(myimg):  
                print "###img:  " 
                print myimg

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
            entity.description = content
            # print name
            # print content
        
        # print entity.convert2Diction()
        json_str = json.dumps(entity.convert2Diction())
        with open('data.json', 'w') as xxf:
            json.dump(entity.convert2Diction(), xxf)

        headers_bdbk = {'Content-Type': 'application/json'}
        request_bdbk = urllib2.Request(url = 'http://127.0.0.1:8000/addfruit', data=json_str, headers=headers_bdbk)
        # response = urllib2.urlopen(request_bdbk)
        # yield entity

            # link = sel.xpath('a/@href').extract()
            # desc = sel.xpath('text()').extract()
            # print desc
            # for gg in sel.xpath("*"):
            #     info = gg.xpath('text()').extract()
            #     for xx in info:
            #         print xx
