import os
import json
import time
import random
import logging
import hashlib
from request_handler import fetch_url
from link_extractor import extract_links
import config
from cache import add_to_set, pop_from_set, set_contains, set_cardinality
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_text(html):
    """Extract readable text from HTML."""
    soup = BeautifulSoup(html, "lxml")
    return soup.get_text(separator="\n", strip=True)

def generate_filename(url):
    """Generate a unique, consistent filename using hashlib."""
    return hashlib.md5(url.encode()).hexdigest() + ".json"

def save_data(url, content):
    """Save extracted text instead of raw HTML."""
    os.makedirs(config.DATA_DIR, exist_ok=True)
    filename = os.path.join(config.DATA_DIR, generate_filename(url))
    clean_text = extract_text(content)
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump({"url": url, "content": clean_text}, file, ensure_ascii=False, indent=4)
        logging.info(f"💾 Data saved for {url} → {filename}")
    except Exception as e:
        logging.error(f"❌ Error saving data for {url}: {e}")

class WebScraper:
    def __init__(self, start_url):
        self.start_url = start_url
        add_to_set("new_urls", start_url)

    def crawl(self):
        """Main scraping loop."""
        logging.info("🔍 Starting Web Scraper...")
        
        while set_cardinality("new_urls"):
            url = pop_from_set("new_urls")
            
            # Skip already processed URLs
            if not url or set_contains("processed_urls", url):
                continue

            add_to_set("processed_urls", url)
            logging.info(f"📌 Scraping: {url}")

            response = fetch_url(url)
            if response and response.status_code == 200:
                save_data(url, response.text)

                new_links = extract_links(response.text, url)
                for link in new_links:
                    if not set_contains("processed_urls", link):
                        add_to_set("new_urls", link)

            # Respect the delay between requests
            delay = random.randint(config.SCRAPER_DELAY_MIN, config.SCRAPER_DELAY_MAX)
            logging.info(f"⏳ Waiting {delay} seconds before next request...")
            time.sleep(delay)
