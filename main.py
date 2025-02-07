import argparse
import glob
import json
import logging
from scraper import WebScraper
from ml_summarizer import summarize_text
import config

def run_pipeline(start_url, keywords, prompt):
    """Runs the scraping and summarization pipeline."""
    print(f"🚀 Starting pipeline for {start_url}")
    scraper = WebScraper(start_url)
    scraper.crawl()
    
    print("✅ Scraping complete! Summarizing...")
    json_files = glob.glob(f"{config.DATA_DIR}/*.json")

    if not json_files:
        print("⚠️ No JSON files found. Scraping might have failed.")
        return
    
    for file in json_files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        text_content = data.get("content", "")
        if not any(keyword.lower() in text_content.lower() for keyword in keywords):
            continue

        summary = summarize_text(text_content, prompt=prompt)
        print(f"📝 Summary for {data.get('url')}:\n{summary}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("website", help="Website URL to start scraping")
    parser.add_argument("--keywords", type=str, help="Comma-separated list of keywords to filter content", default="")
    parser.add_argument("--prompt", type=str, help="Prompt text for summarization", default="")
    
    args = parser.parse_args()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    
    run_pipeline(args.website, keywords, args.prompt)
