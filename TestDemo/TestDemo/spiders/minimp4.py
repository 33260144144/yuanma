# -*- coding: utf-8 -*-
import scrapy
from TestDemo.items import TestdemoItem

class Minimp4Spider(scrapy.Spider):
    name = 'minimp4'
    allowed_domains = ['minimp4.com']
    start_urls = ['http://minimp4.com/?page={}'.format(n) for n in range(10)]

    def parse(self, response):
        #返回的是一个列表
        urls=response.xpath('//div[@class="meta"]/h1/a/@href').extract()
        for url in urls:
            #yield 生成器    callback  回调函数
            yield scrapy.Request(url,callback=self.getContent)

    #主要用于获取数据
    def getContent(selfs,response):
        movieName=response.xpath('//div[@class="movie-meta"]/h1/text()')
        #实例化
        item = TestdemoItem()
        item['name'] = movieName

        yield item