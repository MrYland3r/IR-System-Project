# Movie Review Aggregator and Search Engine

IR-Project for information retrieval (CS 429) - Author: Alexander Silerio

This project is designed to get varied movie reviews from different online sources (currently IMDb), index these reviews for quick searching, and provide a web interface to query reviews. It uses Scrapy for data collection, scikit-learn for data indexing using TF-IDF, and Flask to serve the search queries through a simple interface.

## Requirements

- Python 3.8+
- Scrapy
- scikit-learn
- Flask
- flask-ngrok (for local development)

## Design

The system is built through three main parts (and main.py):
1. **Crawler**: Utilizes Scrapy to navigate IMDb/website and extract movie reviews. (currently not operational, hence non-working)
2. **Indexer**: Employs scikit-learn to create a searchable index of reviews using TF-IDF.
3. **Web Server**: A Flask application that serves the indexed data to the user.

## Architecture
- **Scrapy Spider**: Responsible for scraping data from IMDb.
- **Data Storage**: JSON files.
- **Indexing Service**: Python scripts that process data and create a TF-IDF matrix.
- **Flask API**: Serves the search interface and handles queries.

## Operation
### Commands
- Run Crawler: `python crawler.py`
- Index Data: `python indexer.py`
- Start Server: `python app.py`
- Run All: `python main.py`

## Conclusion
The project sadly does not work in its current state. This originates from the crawler requests being blocked by imdb, but all files are functional per se. More changes required.

## Data Sources
Movie data is scraped from [IMDb Top Charts](https://www.imdb.com/chart/top). (main source of issues with crawler)

## Scripts
```bash
chmod +x build.sh
chmod +x run.sh
```
To execute:
```bash
./build.sh
./run.sh
```

## Source Code
The source code is organized as follows:
- `crawler.py`: Contains the Scrapy spider for IMDb.
- `indexer.py`: Script for indexing scraped data.
- `app.py`: Flask application for serving the search interface.

## Bibliography
- Scrapy Documentation: [Scrapy Official Docs](https://docs.scrapy.org/en/latest/)
- scikit-learn Documentation: [scikit-learn Official Docs](https://scikit-learn.org/stable/)
- Flask Documentation: [Flask Official Docs](https://flask.palletsprojects.com/)
