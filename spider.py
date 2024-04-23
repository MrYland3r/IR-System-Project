import scrapy

class ReviewSpider(scrapy.Spider):
    name = 'review_spider'
    start_urls = ['https://www.imdb.com/chart/top']  # Example start URL

    def parse(self, response):
        for link in response.css('.titleColumn a::attr(href)').extract():
            yield response.follow(link, self.parse_movie)

    def parse_movie(self, response):
        yield {
            'title': response.css('h1::text').get().strip(),
            'review': response.css('.review-content .text::text').get().strip()
        }