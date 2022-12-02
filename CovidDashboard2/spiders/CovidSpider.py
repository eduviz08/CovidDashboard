import scrapy

class CovidSpider(scrapy.Spider):
    name = 'covid'
    start_urls = ['https://www.worldometers.info/coronavirus/#coronavirus-deaths-daily']
    
    custom_settings = {
        'FEEDS': {'data.json': {'format': 'jsonlines', 'overwrite': True}}
        }
	
    def parse(self, response):
#        countries = [response.xpath('//a[@class="mt_a"]/text()').getall()[i] for i in range(227)]
#        yield countries
        for countries in response.xpath('//a[@class="mt_a"]/text()'):
            yield {'countries': countries.get()}




#https://www.worldometers.info/coronavirus/#coronavirus-deaths-daily

#response.xpath('//a[@class="mt_a"]/text()').getall()[0]
#countries = [response.xpath('//a[@class="mt_a"]/text()').getall()[i] for i in range(227)]

#World = [response.xpath('//table[@id="main_table_countries_yesterday2"]/tbody/tr[@class="total_row_world"]/td/text()').getall()[i] for i in range()]


####   response.xpath('//td[@style="font-weight: bold; text-align:right"]/text()').getall()