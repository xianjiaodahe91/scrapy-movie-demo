# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/']

    def parse(self, response):
        movies = response.xpath('//div[@class="list_2"]/ul/li')

        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./a/@title').extract()[0]
            yield item
