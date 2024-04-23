import scrapy
from scrapy.crawler import CrawlerProcess

class MovieReviewSpider(scrapy.Spider):
    name = 'movie_reviews'
    custom_settings = {
        'DEPTH_LIMIT': 3,  #
        'CLOSESPIDER_PAGECOUNT': 100,  
        'AUTOTHROTTLE_ENABLED': True,  
        'AUTOTHROTTLE_START_DELAY': 4,  
        'AUTOTHROTTLE_MAX_DELAY': 60,  
    }

    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        # Extract links to movie details pages
        for link in response.css('.titleColumn a::attr(href)').extract():
            yield response.follow(link, self.parse_movie)

    def parse_movie(self, response):
        # Extract title and reviews from movie details page
        title = response.css('h1::text').get().strip()
        for review in response.css('.review-container'):
            review_text = review.css('.text.show-more__control::text').get()
            if review_text:
                yield {
                    'title': title,
                    'review': review_text.strip()
                }

def run_spider():
    """Function to initiate the spider."""
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'reviews.json',
        'LOG_LEVEL': 'INFO',
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'LOG_LEVEL': 'INFO', 
        'REDIRECT_ENABLED': True,
    '   REDIRECT_MAX_TIMES': 20
    })

    process.crawl(MovieReviewSpider)
    process.start()

if __name__ == '__main__':
    run_spider()