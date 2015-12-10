#### Website: [http://kyang01.github.io/startup-analysis/](http://kyang01.github.io/startup-analysis/)

JKMR Data: Roger Zou, Kevin Yang, Melody Guan, Jerry Anunrojwong

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

#### Startups
We've downloaded our list of startups and their funding round info from [AngelList](https://angel.co/), a US website with extensive startup financial data, and [Crunchbase](https://www.crunchbase.com/), a database of the startup ecosystem. AngelList did not have an API, so we used the urllib2 Requests library to download each search page, then used BeautifulSoup to parse the page. Crunchbase also has no API, so we used the urllib2 Requests library in conjunction with Selenium Webdriver and BeautifulSoup. The data is located in the [startups-data](https://github.com/kyang01/startup-analysis/tree/master/startups-data) folder. The python notebook for scraping AngelList is [here](https://github.com/kyang01/startup-analysis/blob/master/angel-scraping.ipynb) and the python notebook for scraping Crunchbase is [here](https://github.com/kyang01/startup-analysis/blob/master/cb-scraping.ipynb).

#### Tweets
We downloaded our tweets by directly scraping [Twitter](https://twitter.com/) for mentions of startups on our list. While Twitter does have an API, its Search API is limited to an index of 6-9 days of tweets and its Timeline API is limited to up to 3200 tweets per timeline, not to mention rate limits on scraping both. We did initially write a [very messy Python notebook](https://github.com/kyang01/startup-analysis/blob/d98e6455038abec2d97097eb3009fd04c508799d/Mining-the-Social-Web-2nd-Edition/ipynb/Chapter%201%20-%20Mining%20Twitter.ipynb) that used the API, but decided instead to scrape via the Twitter [search page](https://twitter.com/search?q=) with Selenium Webdriver browser scripts and BeautifulSoup. The tweets are located in the [tweets-data](https://github.com/kyang01/startup-analysis/tree/master/tweets-data) folder. The python notebook for scraping Twitter is [here](https://github.com/kyang01/startup-analysis/blob/master/twitter-scraping.ipynb). The python notebook for extracting tweets from BeautifulSoup files to get relevant info is [here](https://github.com/kyang01/startup-analysis/blob/master/twitter-extraction.ipynb).

### Translating Tweets
The majority of our tweets were non-English, necessiting us to translate them in order to get an accurate model that works globally, not just for US startups. After filtering English tweets with the [guess_language](https://bitbucket.org/spirit/guess_language) python library, we used the [Microsoft Translator API](https://pypi.python.org/pypi/microsofttranslator/0.7) to translate all our tweets. The python notebook for running this translation is located [here](https://github.com/kyang01/startup-analysis/blob/master/translate-tweets.ipynb).

# Feature Extraction

### Feature Extraction

### Natural Language Processing
We parsed the text in each tweet using the pattern python library to extract nouns and adjectives. We removed punctuation and stopwords (from sklearn). We decided not to assign topics using LDA due to the heterogeneity of our tweets. We parsed the text into sentences and then tokenized the sentences into words. We then lemmatized the words, which means that we convert words into their basic form, for example: "walk", "walking", "walks", "walked" => "walk". Because each tweet is short (maximum 140 characters) we did not distinguish between sentences within tweets.

### Twitter Sentiment Analysis
We used the sentiment dictionary SentiWordNet 3.0, which assigns to words (both nouns and adjectives) three sentiment scores: positivity, negativity, objectivity. For each tweet, we took the average positivity score over all tokens and the average negativity score over all tokens. We also defined a word as "positive" or "negative" if it had positivity score>0.5 or negativity score>0.5 respectively. For each tweet, we then summed up the total "positive" words and total "negative" words (usually 0,1, and rarely 2). To summarize, we have four features from sentiment analysis: average positivity, average negativity, positive count, negative count. For each company, funding round pair, we then take the average of these features for all their tweets.

# Data Exploration and Feature Selection

### Correlation Analysis 
The features were all normalized using boxcox transformation.

# Results
Who knows lol

# Website
[http://kyang01.github.io/startup-analysis/](http://kyang01.github.io/startup-analysis/)
