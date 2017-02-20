import scrapy

class BuiltInCOSpider(scrapy.Spider):
    name = 'bic'
    start_urls = [
    'http://www.builtincolorado.com/jobs#/jobs?f%5B%5D=im_job_categories%3A78&f%5B%5D=im_job_categories%3A6775&f%5B%5D=im_job_categories%3A8726&f%5B%5D=im_job_categories%3A10010&f%5B%5D=im_job_categories%3A6779&f%5B%5D=im_job_categories%3A6780&f%5B%5D=im_job_categories%3A8223'
    ]

    def parse(self, response):
        for result in response.css('.view-jobs-recent .views-row'):
            yield {
                'company': result.css('.job-company a::text').extract_first(),
                'title': result.css('.job-title a::text').extract_first(),
                'date': result.css('.posted-date::text').extract_first(),
                'url': 'http://builtincolorado.com' + result.css('.job-title a::attr(href)').extract_first(),
            }

        # follow pagination links
        next_page = response.css('.pager .pager-next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
