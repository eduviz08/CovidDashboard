import scrapy
from datetime import date


        
class ourworldNewSpider(scrapy.Spider):
    name = 'ourworldNew'
    allowed_domains = ['ourworldindata.org']
    start_urls = ['https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&zoomToSelection=true&time=2020-03-01..latest&facet=none&uniformYAxis=0&pickerSort=desc&pickerMetric=new_deaths_smoothed&hideControls=false&Metric=Confirmed+deaths&Interval=New+per+day&Relative+to+Population=false&Color+by+test+positivity=false&country=IND~USA~GBR~CAN~DEU~FRA~AFG~Asia']
    
    custom_settings = {
       'FEEDS': {f'ourworldNew_{date.today()}.json': {'format': 'jsonlines', 'overwrite': True}}
       }

    
    def start_requests(self):
        urls = [
            'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&zoomToSelection=true&time=2020-03-01..latest&facet=none&uniformYAxis=0&pickerSort=desc&pickerMetric=new_deaths_smoothed&hideControls=false&Metric=Confirmed+deaths&Interval=New+per+day&Relative+to+Population=false&Color+by+test+positivity=false&country=IND~USA~GBR~CAN~DEU~FRA~AFG~Asia'
            ]        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self,response):
        for row in response.xpath('//*[@class="GrapherComponent GrapherPortraitClass"]/////tbody/tr'):
            yield{
                'Country' : row.xpath('td[1]//text()').extract_first(),
                'New Deaths' : row.xpath('td[2]//text()').extract_first(),
                }
