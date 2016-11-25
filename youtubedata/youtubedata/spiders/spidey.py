# -*- coding: utf-8 -*-
import scrapy
from youtubedata.items import YoutubedataItem

class SpideySpider(scrapy.Spider):
    name = "spidey"
    allowed_domains = ["youtube.com/results?search_query=nerzid"]
    start_urls = (
        'http://www.youtube.com/results?search_query=nerzid/',
    )

    def parse(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        sites = response.xpath("//div[contains(@class,'yt-lockup-video')]//a/@title").extract()
        for site in sites:
			item = YoutubedataItem()
			item['title'] = site
			yield item
