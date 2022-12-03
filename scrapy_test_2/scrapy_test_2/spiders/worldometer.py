import scrapy
from datetime import date


        
class worldometerYesterdaySpider(scrapy.Spider):
    name = 'worldometerYesterday'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']
    
    custom_settings = {
       'FEEDS': {f'worldometerYesterday_{date.today()}.json': {'format': 'jsonlines', 'overwrite': True}}
       }

    
    def start_requests(self):
        urls = [
            'https://www.worldometers.info/coronavirus/',
            ]        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self,response):
        for row in response.xpath('//*[@id="main_table_countries_yesterday"]//tbody/tr'):
            yield{
                'Country' : row.xpath('td[2]//text()').extract(),
                'Cumulative Deaths' : row.xpath('td[5]//text()').extract(),
                'New Deaths' : row.xpath('td[6]//text()').extract(),
                }


class worldometer2DaysagoSpider(scrapy.Spider):    
    name = 'worldometer2Daysago'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']
    
    custom_settings = {
       'FEEDS': {f'worldometer2DaysAgo_{date.today()}.json': {'format': 'jsonlines', 'overwrite': True}}
       }
    
    def start_requests(self):
        urls = [
            'https://www.worldometers.info/coronavirus/',
            ]        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self,response):
        for row in response.xpath('//*[@id="main_table_countries_yesterday2"]//tbody/tr'):
            yield{
                'Country' : row.xpath('td[2]//text()').extract(),
                'Cumulative Deaths' : row.xpath('td[5]//text()').extract(),
                'New Deaths' : row.xpath('td[6]//text()').extract(),
                }
             
        
        
        
        
        
        