# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:24:56 2022

@author: eduvi
"""

import scrapy


class inourworldSpider(scrapy.Spider):
    name = 'inourworldCum'
    start_urls = [
        'https://ourworldindata.org/explorers/'
        ]

    def parse(self, response):
        #all_div_countries = response.css('div.main_table_countries_div')
        #all_a = response.css('a')
        #all_tr_odd = response.css('tr.odd')
        #countries= response.css('td.entity::text').extract()
        all_td = response.css('td.dimension dimension-end')
        cum_deaths = all_td.css('::text').extract()
        
        #countries = all_td.css('a.mt_a::text').extract()
        #deaths = all_td.css
        yield {
            #'countries' : countries
           # 'countries' : countries,
           # 'deaths' : death
           'cumulative deaths' : cum_deaths
            }