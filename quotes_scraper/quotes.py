# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    #allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        self.log('My TEXT HERE !!!!')
        yield {
                
                'author':response.css('small.author::text')[0].extract(),
                'text':response.css('span.text::text')[0].extract()



            }

        
        pass
