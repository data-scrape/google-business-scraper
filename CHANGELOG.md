# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-08-05

### Added
- Initial release of google-business-scraper
- Full scraper implementation with dataclass models
- JSON and CSV export functionality
- CLI with argparse (query, output, format, proxy, limit options)
- Proxy rotation support for anti-bot protection
- Rate limiting and retry logic with exponential backoff
- MIT License
- GitHub Actions CI workflow (Python 3.9-3.12)
- CONTRIBUTING.md and Code of Conduct
- Cross-links to related scraper repositories

### Technical Details
- Python 3.8+ compatibility
- Type hints throughout
- Modular architecture (data models, scraper class, export utilities)
- Error handling with custom exceptions
