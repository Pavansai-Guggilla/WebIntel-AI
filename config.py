import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directory
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Cache directory
CACHE_DIR = os.path.join(BASE_DIR, "cache")
os.makedirs(CACHE_DIR, exist_ok=True)

# Scraper settings
SCRAPER_DELAY_MIN = 5  # Min delay between requests
SCRAPER_DELAY_MAX = 15  # Max delay between requests

print("✅ Configurations loaded successfully!")
