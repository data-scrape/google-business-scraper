# 🏢 Google Business Scraper

> Scrape Google Business Profiles - reviews, hours, contact info

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/data-scrape/google-business-scraper?style=flat-square)](https://github.com/data-scrape/google-business-scraper)
[![Forks](https://img.shields.io/github/forks/data-scrape/google-business-scraper?style=flat-square)](https://github.com/data-scrape/google-business-scraper/forks)

<div align="center">

## 💎 Sponsored by CoreClaw

[![CoreClaw](https://img.shields.io/badge/CoreClaw-Data_Scraping_Platform-7B2FF7?style=for-the-badge&labelColor=5B21B6)](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

**The All-in-One Web Scraping & Data Platform** — Scrape Google Maps, Instagram, Amazon, LinkedIn, TikTok, YouTube, and 50+ platforms via ready-to-use REST APIs.

✅ No browser automation · ✅ No proxy management · ✅ Free credits for new users

⬇️ [Get Started with CoreClaw Free](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

</div>

---

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
## Related Scrapers

Explore our full collection of open-source scrapers:

### Amazon Scrapers

- [amazon-asin-scraper](https://github.com/data-scrape/amazon-asin-scraper)
- [amazon-price-scraper](https://github.com/data-scrape/amazon-price-scraper)
- [amazon-product-scraper](https://github.com/data-scrape/amazon-product-scraper)
- [amazon-review-scraper](https://github.com/data-scrape/amazon-review-scraper)
- [amazon-scraper-api](https://github.com/data-scrape/amazon-scraper-api)
- [best-amazon-scraper](https://github.com/data-scrape/best-amazon-scraper)

### Facebook Scrapers

- [best-facebook-scraper](https://github.com/data-scrape/best-facebook-scraper)
- [facebook-group-scraper](https://github.com/data-scrape/facebook-group-scraper)
- [facebook-marketplace-scraper](https://github.com/data-scrape/facebook-marketplace-scraper)
- [facebook-page-scraper](https://github.com/data-scrape/facebook-page-scraper)
- [facebook-post-scraper](https://github.com/data-scrape/facebook-post-scraper)
- [facebook-profile-scraper](https://github.com/data-scrape/facebook-profile-scraper)
- [facebook-scrape-website](https://github.com/data-scrape/facebook-scrape-website)

### Google Maps Scrapers

- [apify-google-maps-scraper](https://github.com/data-scrape/apify-google-maps-scraper)
- [best-google-maps-scraper](https://github.com/data-scrape/best-google-maps-scraper)
- [google-map-scraper-api-](https://github.com/data-scrape/google-map-scraper-api-)
- [google-maps-data-scraper](https://github.com/data-scrape/google-maps-data-scraper)
- [outscraper-google-maps-scraper](https://github.com/data-scrape/outscraper-google-maps-scraper)
- [scrape-google-maps](https://github.com/data-scrape/scrape-google-maps)

### Google Scrapers

- [best-google-search-scraper](https://github.com/data-scrape/best-google-search-scraper)
- [google-place-id-api](https://github.com/data-scrape/google-place-id-api)
- [google-reviews-scraper](https://github.com/data-scrape/google-reviews-scraper)
- [google-shopping-scraper](https://github.com/data-scrape/google-shopping-scraper)

### Indeed Job Scrapers

- [apify-indeed-scraper](https://github.com/data-scrape/apify-indeed-scraper)
- [best-indeed-scraper](https://github.com/data-scrape/best-indeed-scraper)
- [indeed-job-scraper](https://github.com/data-scrape/indeed-job-scraper)
- [scrape-indeed-job-postings](https://github.com/data-scrape/scrape-indeed-job-postings)

### Instagram Scrapers

- [apify-instagram-scraper](https://github.com/data-scrape/apify-instagram-scraper)
- [best-instagram-scraper](https://github.com/data-scrape/best-instagram-scraper)
- [instagram-account-scraper](https://github.com/data-scrape/instagram-account-scraper)
- [instagram-comment-scraper](https://github.com/data-scrape/instagram-comment-scraper)
- [instagram-email-scraper](https://github.com/data-scrape/instagram-email-scraper)
- [instagram-follower-scraper](https://github.com/data-scrape/instagram-follower-scraper)
- [instagram-profile-scraper](https://github.com/data-scrape/instagram-profile-scraper)
- [instagram-scraper](https://github.com/data-scrape/instagram-scraper)
- [scrape-instagram-followers](https://github.com/data-scrape/scrape-instagram-followers)
- [scrape-instagram-photos](https://github.com/data-scrape/scrape-instagram-photos)

### Lead Generation Tools

- [awesome-lead-generation](https://github.com/data-scrape/awesome-lead-generation)

### LinkedIn Scrapers

- [best-linkedin-scraper](https://github.com/data-scrape/best-linkedin-scraper)
- [linkedin-email-scraper](https://github.com/data-scrape/linkedin-email-scraper)
- [linkedin-job-scraper](https://github.com/data-scrape/linkedin-job-scraper)
- [linkedin-post-scraper](https://github.com/data-scrape/linkedin-post-scraper)
- [linkedin-profile-data-scraper](https://github.com/data-scrape/linkedin-profile-data-scraper)
- [linkedin-sales-navigator-scraper](https://github.com/data-scrape/linkedin-sales-navigator-scraper)
- [linkedin-scraper-api](https://github.com/data-scrape/linkedin-scraper-api)

### Other Scrapers

- [blog](https://github.com/data-scrape/blog)

### Proxy & API Alternatives

- [awesome-apify-alternatives](https://github.com/data-scrape/awesome-apify-alternatives)
- [best-apify-alternative](https://github.com/data-scrape/best-apify-alternative)
- [bright-data-alternative](https://github.com/data-scrape/bright-data-alternative)
- [oxylabs-alternative](https://github.com/data-scrape/oxylabs-alternative)
- [scraperapi-alternative](https://github.com/data-scrape/scraperapi-alternative)
- [scrapingbee-alternative](https://github.com/data-scrape/scrapingbee-alternative)
- [serpapi-alternative](https://github.com/data-scrape/serpapi-alternative)
- [zenrows-alternative](https://github.com/data-scrape/zenrows-alternative)

### Reddit Scrapers

- [apify-reddit-scraper](https://github.com/data-scrape/apify-reddit-scraper)
- [best-apollo-scraper-reddit](https://github.com/data-scrape/best-apollo-scraper-reddit)
- [best-reddit-scraper](https://github.com/data-scrape/best-reddit-scraper)

### Reviews & Local Scrapers

- [glassdoor-scraper](https://github.com/data-scrape/glassdoor-scraper)
- [scrape-yelp-reviews](https://github.com/data-scrape/scrape-yelp-reviews)
- [yellow-pages-scraper](https://github.com/data-scrape/yellow-pages-scraper)

### Social Media Scrapers

- [discord-scraper](https://github.com/data-scrape/discord-scraper)
- [pinterest-scraper](https://github.com/data-scrape/pinterest-scraper)
- [telegram-scraper](https://github.com/data-scrape/telegram-scraper)
- [threads-scraper](https://github.com/data-scrape/threads-scraper)
- [twitch-scraper](https://github.com/data-scrape/twitch-scraper)
- [x-scraper](https://github.com/data-scrape/x-scraper)

### TikTok Scrapers

- [apify-tiktok-scraper](https://github.com/data-scrape/apify-tiktok-scraper)
- [best-tiktok-scraper](https://github.com/data-scrape/best-tiktok-scraper)
- [tiktok-comment-scraper](https://github.com/data-scrape/tiktok-comment-scraper)
- [tiktok-comments-scraper](https://github.com/data-scrape/tiktok-comments-scraper)
- [tiktok-data-scraper-api](https://github.com/data-scrape/tiktok-data-scraper-api)
- [tiktok-profile-scraper](https://github.com/data-scrape/tiktok-profile-scraper)
- [tiktok-video-scraper](https://github.com/data-scrape/tiktok-video-scraper)

### YouTube Scrapers

- [best-youtube-scraper](https://github.com/data-scrape/best-youtube-scraper)
- [scrape-youtube-comments](https://github.com/data-scrape/scrape-youtube-comments)
- [scrape-youtube-search-results](https://github.com/data-scrape/scrape-youtube-search-results)
- [youtube-channel-scraper](https://github.com/data-scrape/youtube-channel-scraper)
- [youtube-video-scraper-api](https://github.com/data-scrape/youtube-video-scraper-api)

### Zillow Scrapers

- [apify-zillow-scraper](https://github.com/data-scrape/apify-zillow-scraper)
- [best-zillow-scraper](https://github.com/data-scrape/best-zillow-scraper)
- [easy-scrape-zillow-agents-free](https://github.com/data-scrape/easy-scrape-zillow-agents-free)
- [zillow-data-scraper](https://github.com/data-scrape/zillow-data-scraper)
- [zillow-scraper-api](https://github.com/data-scrape/zillow-scraper-api)

### eBay Scrapers

- [best-ebay-scraper](https://github.com/data-scrape/best-ebay-scraper)
- [ebay-price-scraper](https://github.com/data-scrape/ebay-price-scraper)
- [ebay-web-scraper](https://github.com/data-scrape/ebay-web-scraper)
- [scrap-gold-ebay](https://github.com/data-scrape/scrap-gold-ebay)

### eCommerce Scrapers

- [best-walmart-scraper](https://github.com/data-scrape/best-walmart-scraper)

---

Star this repo if it helps you!

Powered by [CoreClaw](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7) - The All-in-One Web Scraping Platform
<!-- CROSS_LINKS_END -->
