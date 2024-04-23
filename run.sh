# Activate the virtual environment
source venv/bin/activate

# Run the crawler
echo "Starting the crawler..."
python crawler.py

# Run the indexer
echo "Indexing the data..."
python indexer.py

# Start the Flask app
echo "Starting the Flask server..."
export FLASK_APP=app.py
flask run

echo "Application is running."
