# -*- coding: utf-8 -*-
import scrapy
from pokemoji.items import *


class BulbaSpiderSpider(scrapy.Spider):
    name = "bulba_spider"
    allowed_domains = ["bulbapedia.bulbagarden.net"]
    start_urls = [
        'http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
    ]

    def parse(self, response):
        poke_links = response.xpath('//div[@id="mw-content-text"]//td//a[contains(@href, "Pok%C3%A9mon")]/@href').extract()

        used = set()
        for url in poke_links:
            if url in used: continue
            url = response.urljoin(url)
            used.add(url)
            yield scrapy.Request(url, callback=self.parse_pokemon)

    def parse_pokemon(self, response):
        pokemon = Pokemon()
        name = response.xpath('//table[@class="roundy"][1]//table[1]//td[1]//td[1]//b/text()').extract_first()
        image_urlset = response.xpath('//table[@class="roundy"][1]//a[@class="image"][1]/img/@srcset').extract_first()
        image_url = image_urlset.split(',')[-1].strip().split(' ')[0]
        print image_url

        pokemon['name'] = name
        pokemon['image_urls'] = [image_url]

        if image_url:
            yield pokemon
