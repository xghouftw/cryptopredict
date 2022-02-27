# Sentiment Based Predictions of Cryptocurrencies#

### Welcome to the source code for our project on sentiment based predictions of cryptocurrencies! We all hope you enjoy it as much as we enjoyed working on it!

#### The ultimate design goal was to implement an algorithm capable of predicting Bitcoin, Ethereum, and Dogecoin prices based on historical prices and user text from Google News and Reddit.

Although previous research has been done on the factors influencing cryptocurrency markets, they have largely focused on narrow keyword searches. This project utilizes a wider array of search items to examine connections beyond just cryptocurrencies, such as political and economic factors. We conjecture that this could lend our model increased accuracy and flexibility in its predictive power.

We want for our project to have applications in guiding inexperienced investors with little knowledge of market trends. We wish to help small scale investors make the most out of limited capital, and also to provide a base for future projects related to this topic. 

The project went through five major phases: price data collection, text data collection, sentiment analysis, merging by date, and model training.

#### Price Data Collection
We found and saved publicly available tables for historical crypto statistics, including open, close, and volume. From this data, we calculated daily price change factor as the ratio of close to open. 

#### Text Data Collection
We scraped Google News and Reddit over a two-year time period (1/31/2020 to 1/31/2022), and searched for the keywords 'bitcoin', 'ethereum', 'dogecoin', 'cryptocurrency', 'economy', 'finance', 'politics', and 'pandemic'. For Google News, the pygooglenews API was used to collect article headlines, and for Reddit, the pushshift API was used to collect posts/comments.

#### Sentiment Analysis
We then passed the scraped text data through the Valence Aware Dictionary and sEntiment Reasoner (VADER), which analyzed and scored the sentiment of text of each post with a polarity score ranging from -1 (negative) to 1 (positive). The positive, negative, and neutral components show how the likelihood of some input text being positive, negative, and neutral, respectively. 

#### Merging by Date
Sentiment scores averaged by day for every social medium, keyword, and polarity sign. All columns were appended to the prices spreadsheet so that the corresponding dates matched up.

#### Model Training
A Long Short-Term Memory (LSTM) model was trained to predict 24-hour price changes based on the previous 20 days of crypto prices and social sentiment scores. To mitigate overfitting, the data was separated into training and testing subsets. 
