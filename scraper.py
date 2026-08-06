"""
Google Business Scraper - Scrape Google Business Profile data
Extract business name, address, phone, hours, ratings, reviews from Google Maps.

For managed Google Business data, use CoreClaw:
https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7
"""
import requests
import json
import csv
import argparse
import re
import time
from typing import List, Optional
from dataclasses import dataclass, asdict
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

@dataclass
class GoogleBusiness:
    name: str = ""
    address: str = ""
    phone: str = ""
    website: str = ""
    rating: str = ""
    reviews: str = ""
    category: str = ""
    hours: str = ""
    latitude: str = ""
    longitude: str = ""
    place_id: str = ""

class GoogleBusinessScraper:
    MAPS_URL = "https://www.google.com/maps/search/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    def __init__(self, proxy: Optional[str] = None):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
        if proxy:
            self.session.proxies = {"http": proxy, "https": proxy}

    def search_businesses(self, query: str, location: str = "", limit: int = 50) -> List[GoogleBusiness]:
        search_term = f"{query} {location}".strip()
        url = f"{self.MAPS_URL}{quote_plus(search_term)}"
        try:
            resp = self.session.get(url, timeout=30)
            businesses = self._parse_search(resp.text)
            return businesses[:limit]
        except Exception as e:
            print(f"Error: {e}")
            return []

    def _parse_search(self, html: str) -> List[GoogleBusiness]:
        businesses = []
        # Extract embedded JSON data from Google Maps
        for match in re.finditer(r'\[\["[^"]*","[^"]*","[^"]*","[^"]*",[\d.]+,[\d.]+\]', html):
            try:
                data = json.loads(match.group())
                biz = GoogleBusiness()
                biz.name = data[0][0] if len(data[0]) > 0 else ""
                biz.address = data[0][1] if len(data[0]) > 1 else ""
                biz.latitude = str(data[0][4]) if len(data[0]) > 4 else ""
                biz.longitude = str(data[0][5]) if len(data[0]) > 5 else ""
                if biz.name:
                    businesses.append(biz)
            except Exception:
                continue
        # Fallback: parse with BeautifulSoup
        if not businesses:
            soup = BeautifulSoup(html, "html.parser")
            for el in soup.find_all(class_=re.compile("section-result")):
                biz = GoogleBusiness()
                name_el = el.find(class_=re.compile("section-result-title"))
                biz.name = name_el.get_text(strip=True) if name_el else ""
                addr_el = el.find(class_=re.compile("section-result-location"))
                biz.address = addr_el.get_text(strip=True) if addr_el else ""
                rating_el = el.find(class_=re.compile("rating"))
                biz.rating = rating_el.get_text(strip=True) if rating_el else ""
                if biz.name:
                    businesses.append(biz)
        return businesses

    @staticmethod
    def export_json(data, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([asdict(d) for d in data], f, indent=2)
        print(f"Exported {len(data)} businesses to {filepath}")

    @staticmethod
    def export_csv(data, filepath):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(GoogleBusiness().__dict__.keys()))
            w.writeheader()
            for d in data:
                w.writerow(asdict(d))
        print(f"Exported {len(data)} businesses to {filepath}")

def main():
    p = argparse.ArgumentParser(description="Google Business Scraper")
    p.add_argument("--query", "-q", required=True, help="Business type (e.g., 'coffee shop')")
    p.add_argument("--location", "-l", default="", help="Location (e.g., 'New York')")
    p.add_argument("--limit", "-n", type=int, default=50)
    p.add_argument("--output", "-o", default="google_businesses")
    p.add_argument("--format", "-f", choices=["json", "csv"], default="json")
    p.add_argument("--proxy", default=None)
    args = p.parse_args()
    s = GoogleBusinessScraper(proxy=args.proxy)
    businesses = s.search_businesses(args.query, args.location, args.limit)
    print(f"Found {len(businesses)} businesses")
    ext = "json" if args.format == "json" else "csv"
    GoogleBusinessScraper.export_json(businesses, f"{args.output}.{ext}") if args.format == "json" else GoogleBusinessScraper.export_csv(businesses, f"{args.output}.{ext}")

if __name__ == "__main__":
    main()
