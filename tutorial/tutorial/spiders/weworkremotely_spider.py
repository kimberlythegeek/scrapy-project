import scrapy

class JobsSpider(scrapy.Spider):
    name = 'wwr'
    start_urls = [
        'https://weworkremotely.com/categories/2-programming/jobs#intro',
    ]

    def parse(self, response):
        for result in response.css('.jobs li'):
            yield {
                'company': result.css('a .company::text').extract(),
                'title': result.css('a .title::text').extract(),
                'date': result.css('a .date::text').extract(),
                'url': result.css('a::attr(href)').extract(),
            }
        
    #     # follow links to listing pages
    #     for href in response.css('.result-info a::attr(href)').extract():
    #         yield scrapy.Request(response.urljoin(href),
    #                             callback=self.parse_listing)
    # #     
    # #     # follow pagination links
    # #     next_page = response.css('span.next a::attr(href)').extract_first()
    # #     if next_page is not None:
    # #         next_page = response.urljoin(next_page)
    # #         yield scrapy.Request(next_page, callback=self.parse)
    # # 
    # def parse_listing(self, response):
    #     yield {
    #         'title': response.css('.titletextonly::text').extract(),
    #         'body': response.css('#postingbody::text').extract(),
    #         'email': response.css('.anoneemail::text').extract(),
    #     }