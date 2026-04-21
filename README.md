# Hotel Market Intelligence Web Scraper

## Project Overview
The project was developed to collect hotel data from online sources to support market research for a client in the hospitality industry. The goal was to help the client stay competitive in the market by analyzing hotel listings, pricing, and availability from publicly accessible travel websites.

---

## Project Objectives
- Build an automated scraper to extract hotel listing data  
- Collect pricing and hotel information from travel websites  
- Structure the scraped data into a usable dataset  
- Enable market comparison for competitor analysis  
- Support strategic decision-making for hotel pricing and positioning  

---

## Data Collected
The scraper collects hotel-related data such as:

- Hotel name  
- Location  
- Price per night  
- Ratings and reviews  
- Room availability  
- Listing links  

The data can be used to monitor competitors and analyze pricing trends within the hotel market.

---

## Tools & Technologies
- Python  
- Jupyter Notebook  
- Requests – For sending HTTP requests  
- BeautifulSoup – HTML parsing and data extraction  
- Pandas – Data manipulation and dataset creation  
- CSV / Data export for further analysis  

---

## Project Workflow

### Website Request
The scraper sends HTTP requests to retrieve the HTML content of hotel listing pages.

### HTML Parsing
Using BeautifulSoup, the HTML structure of the page is parsed to locate relevant hotel information.

### Data Extraction
Specific elements such as hotel names, prices, and ratings are extracted from the page.

### Data Cleaning
The extracted data is cleaned and structured into a tabular format using Pandas.

### Data Export
The final dataset is saved as a CSV file for further analysis and reporting.

---

## Potential Business Insights
The collected data can help hotel businesses:

- Monitor competitor pricing strategies  
- Identify market trends in hotel listings  
- Compare ratings and service perception across competitors  
- Optimize pricing strategies  
- Improve their market positioning  

---

## How to Run the Project

### Clone the repository
```
git clone https://github.com/stacie-kipruto/HotelWebScrape.git
```

### Navigate into the project folder
```
cd HotelWebScrape
```

### Install required libraries
```
pip install requests beautifulsoup4 pandas
```

### Run the notebook or script
Open the project notebook or Python script to start scraping hotel data.

---
