import scrapy

class StackOverflowSpider(scrapy.Spider):
    name = 'so'
    start_urls = [
        'http://stackoverflow.com/jobs?l=Remote&d=20&u=Miles&sort=p'
    ]

    def parse(self, response):
        for result in response.css('.jobs div.-job'):
            yield {
                'company': result.css('.-job-info .employer::text').extract_first(),
                'title': result.css('.-job-info .-title .job-link::text').extract_first(),
                'date': result.css('.-job-info .posted::text').extract_first(),
                'url': result.css('.-job-info .-title .job-link::attr(href)').extract_first(),
            }

        # follow pagination links
        next_page = response.css('.pagination .test-pagination-next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
