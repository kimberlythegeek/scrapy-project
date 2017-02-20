import scrapy

class JobsSpider(scrapy.Spider):
    name = 'cg-den'
    start_urls = [
        'https://denver.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1'
    ]

    def parse(self, response):

        # follow links to listing pages
        for href in response.css('.result-info a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                callback=self.parse_listing)

    def parse_listing(self, response):
        yield {
            'title': response.css('#titletextonly::text').extract_first(),
            'date': response.css('#display-date time::text').extract_first(),
            'url': response.request.url
        }