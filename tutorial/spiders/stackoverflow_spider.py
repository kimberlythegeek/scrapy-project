import scrapy

class StackOverflowSpider(scrapy.Spider):
    name = 'so'
    start_urls = [
        'http://stackoverflow.com/jobs?l=Remote&d=20&u=Miles&sort=p'
    ]

    def parse(self, response):
        for result in response.css('.listResults div.-item.-job'):
            yield {
                'company': result.css('div div.fc-black-700.fs-body2::text').extract_first(),
                'title': result.css('div .job-details__spaced .job-link::text').extract_first(),
                'date': result.css('div span.fc-black-500.t24::text').extract_first(),
                'url': 'http://stackoverflow.com/{}'.format(
                    result.css('div .job-details__spaced .job-link::attr(href)').extract_first()
                    ),
            }

        # follow pagination links
        next_page = response.css('.pagination a.test-pagination-next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
