import scrapy

class JobsSpider(scrapy.Spider):
    name = 'wwr'
    start_urls = [
        'https://weworkremotely.com/categories/2-programming/jobs#intro',
    ]

    def parse(self, response):
        for result in response.css('.jobs li'):
            yield {
                'company': result.css('a .company::text').extract_first(),
                'title': result.css('a .title::text').extract_first(),
                'date': result.css('a .date::text').extract_first(),
                'url': result.css('a::attr(href)').extract_first(),
            }
