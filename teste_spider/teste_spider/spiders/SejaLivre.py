# -*- coding: utf-8 -*-
#
import scrapy


class SejalivreSpider(scrapy.Spider):
    # variavel name identifica a spider,deve ser um nome unico no projeto
    name = 'SejaLivre'
    # identifica qual dominio pode seja varrido
    allowed_domains = ['sejalivre.org']
    # url onde a spider vai trabalhar
    start_urls = ['http://sejalivre.org/']

    # metodo que manipula as informacoes extraidas de cada requisicao
    def parse(self, response):
        # busca no seletor <article> e class='post' e lista as informacoes
        # ele busca na classe post por ser a primeira classe referenciada que agrega todos os blocos de noticias
        for resource in response.css("article.post"):
            # o yield retorna o resultado do crawler
            yield {
                'title': resource.css("h2.entry-title a::text").extract(),
                'url': resource.css("h2.entry-title a::attr(href)").extract(),
                'author': resource.css("span.author a::text").extract()
            }