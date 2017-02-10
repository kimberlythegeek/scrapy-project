import scrapy

class JobsSpider(scrapy.Spider):
    name = 'so'
    start_urls = [
        'http://stackoverflow.com/jobs?l=Remote&d=20&u=Miles&sort=p'
    ]

    def parse(self, response):
        for result in response.css('.jobs div.-job'):
            yield {
                'company': result.css('.-job-info .employer::text').extract_first().strip('^\\[rn]$|\s'),
                'title': result.css('.-job-info .-title .job-link::text').extract(),
                'date': result.css('.-job-info .posted::text').extract_first().strip('^\\[rn]$|\s'),
                'url': result.css('.-job-info .-title .job-link::attr(href)').extract(),
            }
        
        # follow links to listing pages
        # for href in response.css('.listResults .-job-info .job-link::attr(href)').extract():
        #     yield scrapy.Request(response.urljoin(href),
        #                         callback=self.parse_listing)
        # 
        # follow pagination links
        next_page = response.css('.pagination .test-pagination-next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
    # 
    # def parse_listing(self, response):
    #     if response.css('h1 .job-link::text').extract():
    #         yield {
    #             'company': response.css('a.employer::text').extract(),
    #             'title': response.css('h1 .job-link::text').extract(),
    #             # 'date': result.css('.posted::text').extract(),
    #             'url': response.request.url
    #         }