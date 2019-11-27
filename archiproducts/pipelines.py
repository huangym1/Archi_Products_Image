# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy

class ArchiproductsPipeline(ImagesPipeline):
	def file_path(self,request,response=None,info=None):
		url = request.url
		file_name = url.split('/')[-1]
		return file_name

	def item_completed(self,results,item,info):
		image_path = [x['path'] for ok, x in results if ok]
		if not image_path:
			raise DropItem("Image Download Failed!")
		return item

	def get_media_requests(self,item,info):
		yield scrapy.Request(item['image_url'])