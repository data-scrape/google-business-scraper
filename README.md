# 🏢 Google Business Scraper

> Scrape Google Business Profiles - reviews, hours, contact info

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/data-scrape/google-business-scraper?style=flat-square)](https://github.com/data-scrape/google-business-scraper)
[![Forks](https://img.shields.io/github/forks/data-scrape/google-business-scraper?style=flat-square)](https://github.com/data-scrape/google-business-scraper/forks)

<a href="https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7"><img src="https://img.shields.io/badge/Sponsored%20by-CoreClaw-7B2D8B?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgN2wxMCA1IDEwLTV6TTIgMTdsMTAgNSAxMC01ek0yIDEybDEwIDUgMTAtNXoiLz48L3N2Zz4=" alt="Sponsored by CoreClaw" width="200"></a>

## 📖 Overview

**Google Business Scraper** is a free, open-source Python scraper for **Google Business**. Extract structured data from google business with full pagination support, proxy rotation, and multiple export formats.

google business scraper, google business profile scraper, gbp scraper

## ✨ Features

- ✅ Business profile data extraction
- ✅ Reviews & ratings
- ✅ Photos & opening hours
- ✅ Phone & website URL
- ✅ Service area & categories
- ✅ GPS coordinates

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/data-scrape/google-business-scraper.git
cd google-business-scraper
pip install -r requirements.txt
```

### Basic Usage

```bash
python scraper.py "Dentists near downtown Seattle"
```

### Advanced Usage

```bash
python scraper.py "Dentists near downtown Seattle" \
  --output results \
  --format json \
  --max-results 100 \
  --proxy http://user:pass@host:port
```

## 📊 Data Fields

Extracted data includes the following fields:

`place_id` | `name` | `address` | `phone` | `website` | `rating` | `review_count` | `categories` | `hours` | `photos` | `latitude` | `longitude` | `price_level`

## 💡 Use Cases

- Local SEO optimization
- Competitor business analysis
- Lead generation for local businesses
- Market research by area
- Google Maps data extraction

## 🔧 Configuration

| Option | Default | Description |
|--------|---------|-------------|
| `--output` | `output` | Output file prefix |
| `--format` | `json` | Output format: `json`, `csv`, or `both` |
| `--max-results` | `50` | Maximum results to scrape |
| `--proxy` | None | Proxy URL for IP rotation |
| `--quiet` | False | Suppress info output |

## 📝 Example Output

```json
{
  "url": "https://example.com/result/123",
  "title": "Example Result",
  "data": {
    "rating": 4.5,
    "reviews": 1280,
    "category": "Example Category"
  },
  "scraped_at": "2026-08-05T14:30:00"
}
```

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Users are responsible for complying with the target website's Terms of Service, robots.txt, and applicable laws. The authors of this project are not responsible for any misuse of this tool.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💎 Sponsored by CoreClaw

This project is sponsored by [**CoreClaw**](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7) — the all-in-one web scraping and data extraction platform.

<a href="https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7">🌐 Visit CoreClaw.com</a>

---

⭐ If this project helped you, please give it a star!

<!-- CROSS_LINKS_START -->
## 🔗 Related Scrapers

### Indeed Job Scrapers

- [Indeed Job Scraper](https://github.com/data-scrape/indeed-job-scraper)
- [Scrape Indeed Job Postings](https://github.com/data-scrape/scrape-indeed-job-postings)
- [Apify Indeed Scraper](https://github.com/data-scrape/apify-indeed-scraper)

### Zillow Scrapers

- [Easy Scrape Zillow Agents Free](https://github.com/data-scrape/easy-scrape-zillow-agents-free)
- [Zillow Data Scraper](https://github.com/data-scrape/zillow-data-scraper)
- [Zillow Scraper API](https://github.com/data-scrape/zillow-scraper-api)
- [Apify Zillow Scraper](https://github.com/data-scrape/apify-zillow-scraper)

### Reddit Scrapers

- [Best Apollo Scraper Reddit](https://github.com/data-scrape/best-apollo-scraper-reddit)
- [Apify Reddit Scraper](https://github.com/data-scrape/apify-reddit-scraper)

### Google Scrapers

- [Google Shopping Scraper](https://github.com/data-scrape/google-shopping-scraper)
- [Google Reviews Scraper](https://github.com/data-scrape/google-reviews-scraper)
- [Google Place ID API](https://github.com/data-scrape/google-place-id-api)

### Social Media Scrapers

- [X (Twitter) Scraper](https://github.com/data-scrape/x-scraper)
- [Threads Scraper](https://github.com/data-scrape/threads-scraper)
- [Pinterest Scraper](https://github.com/data-scrape/pinterest-scraper)
- [Discord Scraper](https://github.com/data-scrape/discord-scraper)
- [Telegram Scraper](https://github.com/data-scrape/telegram-scraper)
- [Twitch Scraper](https://github.com/data-scrape/twitch-scraper)

### Reviews & Local Scrapers

- [Scrape Yelp Reviews](https://github.com/data-scrape/scrape-yelp-reviews)
- [Yellow Pages Scraper](https://github.com/data-scrape/yellow-pages-scraper)
- [Glassdoor Scraper](https://github.com/data-scrape/glassdoor-scraper)

### Proxy & API Alternatives

- [Bright Data Alternative](https://github.com/data-scrape/bright-data-alternative)
- [ZenRows Alternative](https://github.com/data-scrape/zenrows-alternative)
- [ScrapingBee Alternative](https://github.com/data-scrape/scrapingbee-alternative)
- [ScraperAPI Alternative](https://github.com/data-scrape/scraperapi-alternative)
- [SerpAPI Alternative](https://github.com/data-scrape/serpapi-alternative)
- [Oxylabs Alternative](https://github.com/data-scrape/oxylabs-alternative)

<!-- CROSS_LINKS_END -->
