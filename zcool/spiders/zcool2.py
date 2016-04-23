
# -*- coding:utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
import urlparse
from scrapy.http import Request
from scrapy.loader.processors import Join
import json
from zcool.items import ZcoolItem
import sys
from scrapy import *
reload(sys)
sys.setdefaultencoding('utf-8')


class ArticleSpider(Spider):
    name = "zcool"   
    start_urls = [
        "http://www.zcool.com.cn/works/33!0!!0!0!200!1!1!!!/"
    ]

    def parse(self, response):
            
        next = response.xpath('//ul[@class="layout camWholeBoxUl"]/li/a/@href')
        for i in next.extract():
           
            yield Request(i,self.parse_item,dont_filter=False)

    def parse_item(self, response):
        
        item=ZcoolItem()
        item_pic=response.xpath("//div[@class='workShow']/ul/li/div[1]")   
       
        next_item=response.xpath("//a[@class='pageNext']/@href")
        for url in next_item.extract():
            
            yield Request(urlparse.urljoin('http://www.zcool.com.cn',url),self.parse_item,dont_filter=False)
          
        for pic in item_pic:
            item['floder']=response.xpath("//h1[@class='workTitle']/text()").extract()
            item["image_urls"]=pic.xpath("img/@src").extract()
            yield item        
