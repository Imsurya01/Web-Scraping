# Web-Scraping
Scraping Popular Apps data from Google play Store (Python + Selenium)
This project involves scraping the Google Play Store for apps with 5 million or more installs. It utilizes two main phases:

Phase 1: Keyword Scraping

Search Suggestions: Utilize Selenium to extract relevant three-word keyword suggestions from the Google Play Store search bar.
Link Generation: Generate unique app URLs based on each Suggested keyword.


Phase 2: App Data Scraping

Selenium Interaction: Use Selenium to open each generated URL in a browser window(HeadLess Mode).
Data Extraction: Parse the HTML code of each app page to extract relevant data points, including:

App name
Number of installs
Number of reviews
Average rating
App URL
Data Validation: Filtered All the extracted app data, particularly focusing on "installs", "Review" and "Rating".
Data Storage: Save the validated data for each app in a structured format, such as a CSV file (`shaprated).
Overall Flow:

Scrape search suggestions for three-word keywords.
Generate unique app URLs based on the extracted keywords.
For each URL:
Open the app page using Selenium.
Extract relevant data points from the page.
Filtered the data, focusing on "installs", "Review" and "Rating".
Save the validated data in a structured format.
Export the final data as a CSV file.
This approach leverages Selenium's automation capabilities to efficiently extract app data from Google Play Store, focusing specifically on apps exceeding the specified install threshold.
