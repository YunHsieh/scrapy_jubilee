"""
Crawl name : Constellation
create date : 2020/02/13
Author : Jerry
"""


import scrapy
from scrapy_jubilee.items import ScrapyJubileeItem
from datetime import datetime

class click108Spider(scrapy.Spider):
	name = 'click108'
	allowed_domains = ['astro.click108.com.tw']

	def start_requests(self):
		# get today
		self.date_now = datetime.now().strftime('%Y-%m-%d')

		url = "http://astro.click108.com.tw/daily.php"

		# this website using parameters
		parms = {
			"iAcDay" : self.date_now,
			"iAstro" : 12 # constellations
		}

		for i in range(0,parms['iAstro'],1):
			yield scrapy.Request(('%s?iAstro=%s&iAcDay=%s') % (url, i+1, parms['iAcDay']))

	def parse(self, response):

		base_xpath = response.xpath('//div[@class="TODAY_CONTENT"]')[0]
		subtitle_xpath = base_xpath.xpath('./p/span/text()').extract()
		content_xpath = base_xpath.xpath('./p/text()').extract()


		item = ScrapyJubileeItem()
		item['constellation_name']  = base_xpath.xpath('./h3/text()').extract_first()[-5:-2]
		item['overall_score']       = len([_star for _star in subtitle_xpath[0] if _star == '★'])
		item['overall_description'] = content_xpath[0]
		item['love_score']          = len([_star for _star in subtitle_xpath[1] if _star == '★'])
		item['love_description']    = content_xpath[1]
		item['work_score']          = len([_star for _star in subtitle_xpath[2] if _star == '★'])
		item['work_description']    = content_xpath[2]
		item['money_score']         = len([_star for _star in subtitle_xpath[3] if _star == '★'])
		item['money_description']   = content_xpath[3]
		item['date']                = self.date_now
		yield item