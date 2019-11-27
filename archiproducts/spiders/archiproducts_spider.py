# -*- coding: utf-8 -*-
import scrapy
from archiproducts.items import ArchiproductsItem
import re
import sys


# news
class ArchiproductsNewsSpiderSpider(scrapy.Spider):
    name = 'archiproducts_news'
    allowed_domains = ['www.archiproducts.com']
    start_urls = ['http://www.archiproducts.com/en/news']

    def parse(self, response):
        # print(response.text)
        detailSelectors = response.xpath("//div[@class='grid-x grid-padding-x news-container']/div") # 选择器列表
        item = ArchiproductsItem()
        for detailSelector in detailSelectors:
        	detailUrl = self.start_urls[0].split('/en')[0] + detailSelector.xpath(".//a/@href").get()
        	imgUrl = detailSelector.xpath(".//img/@lazy-src").get()
        	item['detail_url'] = detailUrl
        	item['image_url'] = imgUrl
        	yield scrapy.Request(item['detail_url'],callback=self.parse_detail,meta={"item":item})


    def parse_detail(self,response):
    	item = response.meta['item']
    	topImgUrl = response.xpath("//div[@class='cell Article-Gallery']/@style").get().split("(")[1].split(")")[0]
    	imgUrls = response.xpath("//div[@itemprop='articleBody']//img/@lazy-src").getall()
    	item['image_url'] = topImgUrl
    	yield item
    	for imgUrl in imgUrls:
    		item['image_url'] = imgUrl
    		yield item

# Furniture
# Bathroom
# Kitchen
# Lighting
# Outdoor
# Office
# Contract
# Wellness

class ArchiproductsCategorySpider(scrapy.Spider):
    name = 'archiproducts_category'
    allowed_domains = ['www.archiproducts.com']
    start_urls = ['https://www.archiproducts.com/en/products/Bathroom']

    def replace(self,s):
    	regex = re.compile('\D_')
    	s = regex.sub('2b_',s)
    	return s

    def parse(self, response):
        # print(response.text)
        detailSelectors = response.xpath("///div[@class='grid-x grid-padding-x grid-margin-y small-margin-collapse large-up-3 medium-up-2 small-up-1']/div") # 选择器列表
        item = ArchiproductsItem()
        for detailSelector in detailSelectors:
        	try:
	        	detailUrl = self.start_urls[0].split('/en')[0] + detailSelector.xpath("./figure/a/@href").get()
	        	imgUrl = detailSelector.xpath(".//div[@class='img-placeholder']//img/@src").get()
	        	item['detail_1_url'] = detailUrl
	        	item['image_url'] = self.replace(imgUrl)
	        	yield item
	        	yield scrapy.Request(item['detail_1_url'],callback=self.parse_detail_1,meta={"item":item})
	        except Exception as e:
	        	print("{0}信息提取错误 {1}".format(sys._getframe().f_code.co_name,str(e)))

    def parse_detail_1(self, response):
        # print(response.text)
        item = response.meta['item']
        detailSelectors = response.xpath("///div[@class='grid-x grid-padding-x grid-margin-y small-margin-collapse large-up-3 medium-up-2 small-up-1']/div") # 选择器列表
        for detailSelector in detailSelectors:
        	try:
	        	detailUrl = self.start_urls[0].split('/en')[0] + detailSelector.xpath("./figure/a/@href").get()
	        	imgUrl = detailSelector.xpath(".//div[@class='img-placeholder']//img/@src").get()
	        	item['detail_2_url'] = detailUrl
	        	if imgUrl:
	        		item['image_url'] = self.replace(imgUrl)
	        		yield item
	        	yield scrapy.Request(item['detail_2_url'],callback=self.parse_detail_2,meta={"item":item})
	        except Exception as e:
	        	print("{0}信息提取错误 {1}".format(sys._getframe().f_code.co_name,str(e)))

    def parse_detail_2(self,response):
    	item = response.meta['item']
    	detailSelectors = response.xpath("//div[@class='grid-x grid-padding-x grid-margin-y large-up-3 medium-up-2 small-up-2']/div")
    	for detailSelector in detailSelectors:
    		try:
	    		detailUrl = self.start_urls[0].split('/en')[0] + detailSelector.xpath(".//a/@href").get()
	    		imgUrl = detailSelector.xpath(".//img/@lazy-src").get()
	    		item['detail_3_url'] = detailUrl
	    		if imgUrl:
	    			item['image_url'] = self.replace(imgUrl)
	    			yield item
	    		yield scrapy.Request(item['detail_3_url'],callback=self.parse_detail_3,meta={"item":item})
	    	except Exception as e:
	    		print("{0}信息提取错误 {1}".format(sys._getframe().f_code.co_name,str(e)))


    def parse_detail_3(self,response):
    	item = response.meta['item']
    	imgUrls = response.xpath("//div[@class='item item-small']/img/@lazy-src").getall()
    	for imgUrl in imgUrls:
    		item['image_url'] = self.replace(imgUrl)
    		yield item
