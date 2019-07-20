# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    ##start_urls = ['http://meijutt.com/']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        ##movies = response.xpath('//div[@class="list_2"]/ul/li')
        movies = response.xpath('//li/div[@class="lasted-num fn-left"]')
        items = []

        print "siyang==================="
        print response
        print movies

        for each_movie in movies:
          item = MovieItem()
          item["storyName"]  = each_movie.xpath('../h5/a/text()').extract()[0]
          item["storyState"] = each_movie.xpath('../span[@class="state1 new100state1"]/font/text()').extract()[0]
          item['tvStation']  = each_movie.xpath('../span[@class="mjtv"]/text()').extract()
          item['updateTime'] = each_movie.xpath('//div[@class="lasted-time new100time fn-right"]/text()').extract()[0]

          print item["storyName"], item["storyState"], item["tvStation"], item["updateTime"]
          yield item

          ##item = MovieItem()
          ##item['name'] = each_movie.xpath('./a/@title').extract()[0]
          ##yield item


