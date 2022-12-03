import scrapy
from datetime import date

class WHOlatestSpider(scrapy.Spider):
     name = 'WHOlatest'
     allowed_domains = ['who.int']
     start_urls = ['https://covid19.who.int/table']
     
     custom_settings = {
        'FEEDS': {f'WHOlatest{date.today()}.json': {'format': 'jsonlines', 'overwrite': True}}
        }
 
     
     def start_requests(self):
         urls = [
             'https://covid19.who.int/table'
             ]        
         for url in urls:
             yield scrapy.Request(url=url, callback=self.parse)
             
     def parse(self,response):
         for row in response.xpath('//*[@class="tbody"]'):
             yield{
                 'Country' : row.xpath('div[@class="column_name td"]::text').extract(),
                 #'New Deaths' : row.xpath('td[3]/span//text()').extract(),
                 }


# =============================================================================
# class WHOlatestSpider(scrapy.Spider):
#     name = 'WHOlatest'
#     start_urls = [
#         'https://covid19.who.int/table'
#         ]
#     
#     custom_settings = {
#             'FEEDS': {f'WHOlatest{date.today()}.json': {'format': 'jsonlines', 'overwrite': True}}
#             }
#     
#     def parse(self,response):
#         all_div_tr = response.css('div.tr.depth_0')
#         
#         for rows in all_div_tr:
#             Country = all_div_tr.css('div.column_name.td::text').extract()
#             CumulativeDeaths = all_div_tr.css('div.column_Cumulative_Deaths.td::text').extract()
#             NewDeaths = all_div_tr.css('div.column_Deaths.td::text').extract()
#             
#             yield{
#                 'Country' : Country,
#                 'Cumulative Deaths' : CumulativeDeaths,
#                 'New Deaths' : NewDeaths,
#                 }
# =============================================================================
