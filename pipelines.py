# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ToscrapeXpathPipeline(object):
    def __init__(self):
        self.file = open('item.json','wb')
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item
