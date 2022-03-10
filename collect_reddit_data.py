# -*- coding: utf-8 -*-
"""
reddit_collector.py
reddit data collection script
Usage: reddit_collector.py
Example: python3 reddit_collector.py
"""

"""
Description: Data from the following list of search terms will be collected from reddit:
{Bitcoin, Ethereum, Dogecoin, Cryptocurrency}
For each term, a request will be sent to the pushshift API to collect a random sample of
comments for every day, starting from two years ago
The API returns a JSON formatted string, which can be converted to a dictionary by using
the requests.json() method.
This new dictionary has the 'data' key and sometimes the 'metadata' key.
The Pandas library is used to convert the dictionary into a DataFrame,
which is then written to a .csv file.
"""

import sys
import requests
import pandas as pd
import json
import datetime
import time

'''
class Collector:
  def __init__(self, start_date: datetime.datetime, end_date: datetime.datetime, 
               max_daily_size: int, queries: list = ['bitcoin', 'ethereum', 'dogecoin', 
              'cryptocurrency', 'economy', 'finance', 'politics', 'pandemic'], data: list = []):
    self.start_date = start_date
    self.end_date = end_date
    self.max_daily_size = max_daily_size
    self.queries = queries
    self.data = []
class RedditCollector:
  def __init__(self, start_date: datetime.datetime, end_date: datetime.datetime, max_daily_size: int, queries: list, data: list = []):
    super(self, start_date: datetime.datetime, end_date: datetime.datetime, max_daily_size: int, queries: list, data: list = [])
  def collect_data():
    # TODO
    # Collect data within date range according to parameters
    # Exclude Bot comments
    # Collect top comments for each day
    for query in self.queries:
        pass
  def process_data(self):
    # TODO
'''


def query_reddit(search_queries: list = None, subreddit: str = None, from_date: int = None, until_date: int = None,
                 size: int = 100):
    # return a list of dictionaries, each dictionary contains data for one comment
    JSONDecodeError = True
    print(from_date)
    comments = []
    for query in search_queries:
        count = 0
        while JSONDecodeError and count < 10:
            print(query + "\t", count)
            count += 1
            search_query_url = "https://api.pushshift.io/reddit/search/comment/?q=" + query + "&subreddit=" + subreddit + "&before=" + str(
                until_date) + "d&after=" + str(from_date) + "d&size=" + str(size)
            data = requests.get(search_query_url)
            try:
                comments_data = data.json()
                comments.extend(comments_data['data'])
                break
            except:
                pass
            time.sleep(1)
    return comments


def main(filepath, date_range, topics, words_of_interest) -> None:
    """
    :param filepath:
    :param topics:
    :return:
    """

    for topic in topics:
        # Import all data from reddit first
        print("Collecting reddit data for: " + topic + "\nStretching " + str(date_range) + " days back in time")
        topic_data = [
            query_reddit(search_queries=words_of_interest[topic], subreddit=topic, from_date=x + 1, until_date=x) for x
            in range(date_range, 0, -1)]

        print("Done collecting " + topic + " data.\nWriting to JSON file...")
        with open(filepath + "reddit-" + topic + ".json", "w") as out_file:
            json.dump(topic_data, out_file, indent=4)

        print("Creating dictionary mappings...")
        data_dict = {'text': [], 'date': [], 'unix_time': [], 'score': [], 'num_awards': []}
        for i, daily_comments in enumerate(topic_data):
            temp_date = date_range - i
            for comment in daily_comments:
                data_dict['text'].append(comment['body']) if len(comment['body']) > 0 else data_dict['text'].append(
                    'null')
                data_dict['date'].append(temp_date)
                data_dict['unix_time'].append(comment['created_utc']) if len(str(comment['created_utc'])) > 0 else \
                    data_dict['unix_time'].append('null')
                data_dict['score'].append(comment['score']) if len(str(comment['score'])) > 0 else data_dict[
                    'score'].append('null')
                data_dict['num_awards'].append(comment['total_awards_received']) if len(
                    str(comment['total_awards_received'])) > 0 else data_dict['num_awards'].append('null')
        df = pd.DataFrame(data_dict)
        df['is_not_a_bot'] = df['text'].apply(lambda text: is_not_a_bot(text))
        df = df[df['is_not_a_bot']]
        print("Writing to csv...")
        df.to_csv(filepath + "reddit-" + topic + ".csv", index=False)
        print("Done!!\n\n\n")


def is_not_a_bot(text):
    return not ("I am a bot" in text)


if __name__ == "__main__":
    # IMPORTANT!! CURRENT DATE: 03/08/2022

    script, topics = sys.argv
    topics = topics.split()
    # date_range = int(date_range)
    date_range = 800

    words_of_interest = {'cryptocurrency': ['moon', 'crypto', 'blockchain', 'bearish',
                                            'bullish', 'growth', 'going', 'market'],
                         'bitcoin': ['moon', 'crypto', 'blockchain', 'bearish',
                                     'bullish', 'growth', 'going', 'market'],
                         'ethereum': ['moon', 'crypto', 'blockchain', 'bearish',
                                      'bullish', 'growth', 'going', 'market'],
                         'dogecoin': ['moon', 'crypto', 'blockchain', 'bearish',
                                      'bullish', 'growth', 'going', 'market'],
                         'politics': ['war', 'ban', 'price', 'conflict', 'agreement',
                                      'peace', 'end', 'environment', 'justice'],
                         'finance': ['market', 'stocks', 'growth', 'trend', 'capital',
                                     'shares', 'crash', 'momentum'],
                         'economy': ['economy', 'saving', 'demand', 'currency',
                                     'supply', 'inflation', 'finance', 'goods'],
                         'pandemic': ['COVID', 'disease', 'coronavirus', 'virus',
                                      'epidemic', 'vaccine', 'population']
                         }

    # collect all relevant data in one dataframe and store it as a csv
    # queries = [bitcoin, ethereum, dogecoin, cryptocurrency, economy, politics, finance, pandemic]
    filepath = './'
    main(filepath, date_range, topics, words_of_interest)
