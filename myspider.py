# -*- coding:utf-8 -*-
import scrapy
from mytest.items import MytestItem
class MySpider(scrapy.Spider):
    name='sspider'
    allowed_domains = ["dress.pclady.com.cn"]
    start_urls = ["http://dress.pclady.com.cn/stature/"]
    def parse(self, response):
        items=[]
        result=response.xpath('//li/i[@class="iPic"]')

        for info in result:
            item=MytestItem()
            #item['url']=[]
            #t=result.xpath('a/@href').extract()[0]
            #item['url'].append(t)
            item['url']=info.xpath('a/@href').extract()
            items.append(item)
            yield item
        next_page = response.xpath('//a[@class="next"]/@href')
        if next_page:
            # 爬每一页
            yield scrapy.Request(next_page[0].extract(), self.parse)


    # 翻页
