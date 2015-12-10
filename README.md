#### Website: [http://kyang01.github.io/startup-analysis/](http://kyang01.github.io/startup-analysis/)

JKMR Data

# Predicting Startup Funding Rounds via Tweets

For the average public relations officer, manipulating the media is a standby. Social media is no exception, with sites like Twitter, Instagram, and Facebook now regular tools in a publicist's arsenal. Raising brand awareness and positive sentiment may be especially important before important events like a startup's Series B. We propose to test the converse: Before financing rounds, might there be an abnormal amount of PR activity? Can we predict details on events like financing rounds based on mentions of a company on social media platforms like Twitter?

This project tests our hypothesis by *model description here*. 

# Overview of Procedure

1. Data Collection and Cleaning
- Scraping Twitter and AngelList
- Translating foreign language tweets
2. Feature Extraction
- Feature Extraction
- NLP
- Twitter Sentiment Analysis
3. Data Exploration and Feature Selection
- Correlation Analysis 
- PCA
4. Predictive Modeling
- Linear Regression
- SVM
5. Presentation
- Website

# Data Collection
We've downloaded our list of startups and their funding round info from [AngelList](https://angel.co/), a US website with extensive startup financial data, and [Crunchbase](https://www.crunchbase.com/), a database of the startup ecosystem. AngelList did not have an API, so we used the urllib2 Requests library to download each search page, then used BeautifulSoup to parse the page. Crunchbase also has no API, so we used the urllib2 Requests library in conjunction with Selenium Webdriver and BeautifulSoup. The data is located in the [startups-data](https://github.com/kyang01/startup-analysis/tree/master/startups-data) folder. The python notebook for scraping AngelList is [here](https://github.com/kyang01/startup-analysis/blob/master/angel-scraping.ipynb) and the python notebook for scraping Crunchbase is [here](https://github.com/kyang01/startup-analysis/blob/master/cb-scraping.ipynb).

We downloaded our tweets by directly scraping Twitter via the Twitter search page for mentions of startups.

# Feature Extraction

# Results
Who knows lol
