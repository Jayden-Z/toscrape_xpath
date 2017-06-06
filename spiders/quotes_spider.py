#conding = utf-8

from scrapy import Spider
from toscrape_xpath.items import ToscrapeXpathItem

class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com'
    ]
    def parse(self, response):
        for sel in response.xpath('//div[@class = "quote"]'):
            item = ToscrapeXpathItem()
            item['author'] = sel.xpath('span[2]/small/text()').extract()
            item['text'] = sel.xpath('span[1]/text()').extract()
            item['tag'] = sel.xpath('div/a/text()').extract()
            yield item
