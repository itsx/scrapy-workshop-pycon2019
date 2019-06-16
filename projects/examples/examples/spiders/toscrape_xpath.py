# -*- coding: utf-8 -*-
import scrapy


class ToscrapeXpathSpider(scrapy.Spider):
    name = 'toscrape-xpath'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'test': quote.xpath("/span[@class='text']/text()").extract(),
                'author': '',
                'tags': '',
            }
            #  /span[@class='text']/text()").extract()
        pass
