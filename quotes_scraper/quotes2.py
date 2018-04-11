# -*- coding: utf-8 -*- 
import scrapy


class Quotes2Spider(scrapy.Spider):
    name = 'quotes2'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']

    def parse(self, response):
        for each in response.css('div.quote'):
            #self.log(type(each))
            yield {'author':each.css('div.quote > span >small.author::text').extract(),
                    'text':each.css('div.quote > span.text::text').extract()

                }




        
                
        
