# -*- coding: utf-8 -*-
#
import scrapy


class SejalivreSpider(scrapy.Spider):
    name = 'SejaLivre'
    allowed_domains = ['sejalivre.org']
    start_urls = ['http://sejalivre.org/']

    def parse(self, response):
        article = response.css(".entry-title").xpath('//a[@rel="bookmark"]/text()').extract()
        author = response.css(".entry-title").xpath('//a[@rel="author"]/text()').extract()
        link = response.css(".entry-title a::attr(href)").extract()

        for i in article:
            print(i)

        for j in author:
            print(j)

        for k in link:
            print(k)
