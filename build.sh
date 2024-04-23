# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the required packages
pip install Scrapy scikit-learn Flask

echo "Build completed successfully."
