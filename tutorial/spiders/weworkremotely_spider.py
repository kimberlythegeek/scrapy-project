import scrapy

class JobsSpider(scrapy.Spider):
    name = 'wwr'
    start_urls = [
        'https://weworkremotely.com/categories/2-programming/jobs#intro',
    ]

    def parse(self, response):

        # follow links to listing pages
        for href in response.css('.jobs li a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                callback=self.parse_listing)

    def parse_listing(self,response):
        yield {
            'company': response.css('h2 .company::text').extract_first(),
            'title': response.css('.listing-header-container h1::text').extract_first(),
            'date': response.css('.listing-header-container h3::text').extract_first(),
            'url': response.request.url
        }
