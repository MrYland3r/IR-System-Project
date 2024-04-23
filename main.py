from crawler.spider import ReviewSpider
from indexer.index import indexer
from scrapy.crawler import CrawlerProcess
from webapp.app import app

def run_crawler():
    process = CrawlerProcess()
    process.crawl(ReviewSpider)
    process.start()  # the script will block here until the crawling is finished

def run_indexer():
    # Assume documents are saved from the crawler output
    indexer = Indexer()
    documents = ["Sample movie review 1", "Sample movie review 2"]
    indexer.create_index(documents)

if __name__ == '__main__':
    run_crawler()
    run_indexer()
    app.run()  # Start Flask app