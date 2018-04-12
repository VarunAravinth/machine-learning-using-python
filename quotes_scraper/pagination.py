# -*- coding: utf-8 -*- 
import scrapy


class Quotes2Spider(scrapy.Spider):
    name = 'quotes2'
    #allowed_domains = ['toscrape.com']
    s='http://quotes.toscrape.com/page/'
    start_urls = ['http://quotes.toscrape.com/page/1/']
    for i in range(2,6):
        s1=s+str(i)+'/'
        start_urls.append(s1)
    
    
    

    def parse(self, response):
        for each in response.css('div.quote'):
            #self.log(type(each))
            yield {'author':each.css('div.quote > span >small.author::text').extract(),
                    'text':each.css('div.quote > span.text::text').extract()

                }
            
        #relative_url = response.css('li.next > a::attr(href)').extract_first() #/page/2/     
        #full_url = response.urljoin(relative_url)
        #yield scrapy.Request(url=full_url,callback = self.parse)
        



