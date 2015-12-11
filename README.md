#### Website: [http://kyang01.github.io/startup-analysis/](http://kyang01.github.io/startup-analysis/)
#### Screenshare: [http://youtu.be/4JwMyLHcCYI?hd=1](http://youtu.be/4JwMyLHcCYI?hd=1)
JKMR Data: Roger Zou, Melody Guan, Kevin Yang, Jerry Anunrojwong

# Predicting Startup Funding Rounds via Tweets

For the average public relations officer, manipulating the media is a standby. Social media is no exception, with sites like Twitter, Instagram, and Facebook now regular tools in a publicist's arsenal. Raising brand awareness and positive sentiment may be especially important before important events like a startup's Series B. We propose to test the converse: Before financing rounds, might there be an abnormal amount of PR activity? Can we predict details on events like financing rounds based on mentions of a company on social media platforms like Twitter? Or is social media a noisy, meaningless indicator?

This project aims to use data analysis and predictive analytics to find correlations between tweets and startup funding rounds in order to shed light on potential importance of tweets and social media in general as indicators of startup success. Through a variety of models, we show that there is unfortunately minimal relationship between tweets and startup funding.

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
We parsed the text in each tweet using the pattern python library to extract nouns and adjectives. We removed punctuation and stopwords (from sklearn). We decided not to assign topics using LDA due to the heterogeneity of our tweets. We parsed the text into sentences and then tokenized the sentences into words. We then lemmatized the words, which means that we convert words into their basic form, for example: "walk", "walking", "walks", "walked" => "walk". Because each tweet is short (maximum 140 characters) we did not distinguish between sentences within tweets. Code for NLP can be found [here](https://github.com/kyang01/startup-analysis/blob/master/Melody%20Twitter%20Sentiment%20Analysis.ipynb).

### Twitter Sentiment Analysis
We used the sentiment dictionary SentiWordNet 3.0, which assigns to words (both nouns and adjectives) three sentiment scores: positivity, negativity, objectivity. For each tweet, we took the average positivity score over all tokens and the average negativity score over all tokens. We also defined a word as "positive" or "negative" if it had positivity score>0.5 or negativity score>0.5 respectively. For each tweet, we then summed up the total "positive" words and total "negative" words (usually 0,1, and rarely 2). To summarize, we have four features from sentiment analysis: average positivity, average negativity, positive count, negative count. For each company, funding round pair, we then take the average of these features for all their tweets. The python notebook for twitter sentiment analysis is [here](https://github.com/kyang01/startup-analysis/blob/master/Melody%20Twitter%20Sentiment%20Analysis.ipynb).


# Data Exploration and Feature Selection

### Correlation Analysis 
We plotted the unscaled 'Amount Raised' against all unscaled numerical features, and found no linear correlations. We then plotted the unscaled 'Amount Raised' against all numerical features normalized using boxcox transformation, and again found no linear correlations. We did not find linear correlations for scaled 'Amount Raised' against unscaled features either. We did find some homoskedastic correlations for scaled 'Amount Raised' against scaled features', but unfortunately these slopes were flat. From our correlation analysis, we infer that using SVR may be a better method for predictive modeling than linear regression. Code for correlation analysis is [here](https://github.com/kyang01/startup-analysis/blob/master/Correlation%20Analysis.ipynb).

### PCA 
Principal Component Analysis (PCA) tries to isolate a handful of linear combinations of features that "explain" most variances in the data. This is a descriptive, not predictive, technique, and it operates on the whole dataset without the training/testing division. Moreover, PCA is more informative if all features are suitably normalized, so no single feature can dominate the total variance. We then use Box Cox transformation on each column (the library chooses an appropriate parameter, different for each column, to make the resulting transformation approximately Normal.) The exception is the funding raised, which we use the log transformation (which is also a special case of Box Cox). This is justified because our plot shows that log(funding) looks Normal, and when we predict log(funding), reversing the function to get funding is more expedient. Our PCA shows that only a few (aggregated) features explain most of the variance. 3 top features explain 95% of the variance, while 5 top features explain 98% of the variance. The python notebook for PCA is [here](https://github.com/kyang01/startup-analysis/blob/master/pca-and-svr.ipynb).


# Predictive Modeling

### Linear Regression

### SVR

We suspect that the problem is not linear, so we turn to Support Vector Regression (SVR).  We split the data into the training data and the testing data, standardize the numerical features of each of the two datasets separately. We try three choices of kernels - rbf, linear and polynomial. For each choice of kernal, we use GridSearchCV with 5-fold cross validation to find the optimal parameters of the predictor over a reasonable (pre-determined) range of parameters. We then fit the predictor to the training data, predict it on the test data, and evaluate it by computing RMSE on log(funding). We found that rbf predictor with C=100 and gamma=0.01 is the best, with RMSE around 1. This result is comparable to linear regression. The python notebook for PCA is [here](https://github.com/kyang01/startup-analysis/blob/master/pca-and-svr.ipynb) (same notebook as PCA).

### Neural Nets

In order to explore other methods that can identify nonlinear trends, we wanted to run neural nets as well. Similar to the previous example, we used normalized variations of numerical data. The data we wanted to predict was the log of the series funding amounts. We worked with various python neural net libraries with limited success. Ultimately, we decided to work with Matlab to create a neural net. We used the neural net toolbox and created a neural net with one layer of 50 intermediate nodes. The neural net package provided by Matlab uses the Levenberg-Marquadrt algorithm to run. In the end, we were able to achieve an RMSE of 18.8.

# Website
[http://kyang01.github.io/startup-analysis/](http://kyang01.github.io/startup-analysis/)
