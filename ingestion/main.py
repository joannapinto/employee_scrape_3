import json
import os
from scraper import run_scraper

def main(scraper_id):
    config_path = os.path.join("ingestion", "run_scraper.json")

    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}")
        return

    with open(config_path, 'r') as f:
        config = json.load(f)

    scrapers = config.get("scrapers", [])
    url = None
    for scraper in scrapers:
        if scraper.get("scraper_id") == scraper_id:
            url = scraper.get("scraper_name")
            break

    if not url:
        print(f"Scraper ID '{scraper_id}' not found in config.")
        return

    print(f"Running scraper '{scraper_id}' on URL: {url}")
    run_scraper(url)
    print("Scraper completed successfully.")

if __name__ == "__main__":
    main(scraper_id="emp1")  # change to emp2 if needed
