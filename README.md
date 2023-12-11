## Google Play Store Popular Apps Scraper

This project utilizes Python and Selenium to scrape app data from the Google Play Store, focusing on all popular apps with **"App Name", "Rating","Reviews", "Downloads" and "App link"**.

### Requirements

* Python 3.6+
* Selenium
* ChromeDriver
* BeautifulSoup4

### Installation

1. Install the required libraries:

```bash
pip install selenium beautifulsoup4
```

2. Download the ChromeDriver corresponding to your Chrome version: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

### Usage

1. Open a terminal and navigate to the project directory.
2. Run the script: by Step wise 

```bash
python app_scraper.py
```

### Data Output

The script generates a CSV file named `shaprated.csv` containing the following data for each scraped app:

* App Name
* Number of Installs
* Number of Reviews
* Average Rating
* App URL

### Structure

* `app_scraper.py`: Main script for scraping and data extraction.
* `utils.py`: Utility functions for Selenium interaction and data manipulation.
* `chromedriver.exe`: ChromeDriver executable (download and configure path).
* `README.md`: This file.

### Notes

* This script focuses on scraping apps with **three-word keyword searches**.
* You can modify the script to customize the search criteria and extracted data points.
* Consider implementing headless mode in Selenium for faster execution.
* Be aware of Google's Terms of Service regarding scraping and act responsibly.
