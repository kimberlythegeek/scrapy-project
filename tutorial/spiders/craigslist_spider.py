import scrapy

class JobsSpider(scrapy.Spider):
    name = 'cg'
    start_urls = [
        'http://atlanta.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://austin.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://boston.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://chicago.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://dallas.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://denver.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://detroit.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://houston.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://lasvegas.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://losangeles.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://miami.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://minneapolis.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://newyork.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://orangecounty.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://philadelphia.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://phoenix.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://portland.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://raleigh.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://sacramento.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://sandiego.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://seattle.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://sfbay.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
        'http://washingtondc.craigslist.org/search/jjj?excats=12-1-2-1-7-1-1-1-1-1-19-1-1-3-2-1-2-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1',
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