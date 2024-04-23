from crawler import run_spider
from indexer import index_review
from app import app
import threading

def main():
    run_spider()  # Run the spider to scrape data
    index_review()  # Index the scraped data
    threading.Thread(target=lambda: app.run(debug=True)).start()  # Run Flask app

if __name__ == '__main__':
    main()