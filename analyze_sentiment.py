import pandas as pd
!pip install vaderSentiment
from google.colab import drive
drive.mount('/content/drive')
path = "/content/drive/MyDrive/archive.zip (Unzipped Files)/Bitcoin_tweets.csv"
df = pd.read_csv(path)

df = df.dropna()
textcolumn = df.loc[:,"text"]
sentlistneg = []
sentlistneu = []
sentlistpos = []
sentlistcom = []

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid_obj = SentimentIntensityAnalyzer()

def VADER(sentence):
  sentiment_dict = sid_obj.polarity_scores(sentence)
  sentlistneg.append(sentiment_dict['neg'])
  sentlistneu.append(sentiment_dict['neu'])
  sentlistpos.append(sentiment_dict['pos'])
  sentlistcom.append(sentiment_dict['compound'])

i = 0
for comment in textcolumn:
  VADER(comment)
print(i)

df["Neg"] = sentlistneg
df["Neu"] = sentlistneu
df["Pos"] = sentlistpos
df["Com"] = sentlistcom

df.to_csv("scores.csv")
