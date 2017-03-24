# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SectionItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    image_urls = scrapy.Field()

    def convert2Diction(self):
        dic = {"title":self['title'], "content":self['content']}
        return dic
    pass

class BdbkItem():
    # define the fields for your item here like:
    name = str()
    discription = str()
    section = []
    image = str

    def convert2Diction(self):
        dic = {}
        dic["name"] = self.name
        dic["discription"] = self.discription
        itemlist = []
        for item in self.section:
            if isinstance(item, SectionItem):
                itemlist.append(item.convert2Diction())
        dic["section"] = itemlist
        return dic
    pass


