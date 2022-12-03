import scrapy


        
        
class worldometerSpider(scrapy.Spider):
    name = 'worldometer'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def start_requests(self):
        urls = [
            'https://www.worldometers.info/coronavirus/',
            ]        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self,response):
        #for row in response.xpath('//table[@id="main_table_countries_yesterday"]//tbody/tr/td/a[@class="mt_a"]'):
        #for row in response.xpath('//*[@class="mt_a"]'):
        for row in response.xpath('//*[@id="main_table_countries_yesterday"]//tbody/tr'):
            yield{
                'Country' : row.xpath('td[2]//text()').extract(),
                'Cumulative Deaths' : row.xpath('td[5]//text()').extract(),
                'New Deaths' : row.xpath('td[6]//text()').extract(),
                }
        


        
      
        
        
        
        
        
        
        
        
        
        
        