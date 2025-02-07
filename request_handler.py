# scraper/request_handler.py
import requests
from fake_useragent import UserAgent
import logging
import time

ua = UserAgent()

def fetch_url(url, retries=3, backoff_factor=2):
    """Fetch URL with retry logic, random User-Agent, and exponential backoff."""
    headers = {'User-Agent': ua.random}
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            print(f"✅ Successfully fetched: {url}")
            return response
        except requests.RequestException as e:
            print(f"⚠️ Attempt {attempt + 1} failed for {url}: {e}")
            time.sleep(backoff_factor * (2 ** attempt))
    print(f"❌ Failed to fetch {url} after {retries} attempts.")
    return None