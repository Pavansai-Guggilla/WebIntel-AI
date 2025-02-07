# scraper/link_extractor.py
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def extract_links(html, base_url):
    """Extract valid links restricted to the base domain."""
    soup = BeautifulSoup(html, "lxml")
    base_domain = urlparse(base_url).netloc
    links = {urljoin(base_url, a["href"]) for a in soup.find_all("a", href=True) if urlparse(urljoin(base_url, a["href"])).netloc == base_domain}
    
    print(f"🔗 Extracted {len(links)} links from {base_url}")
    return list(links)
