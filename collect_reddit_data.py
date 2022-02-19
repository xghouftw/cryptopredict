# -*- coding: utf-8 -*-
"""
reddit_collector.py
reddit collector script

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
import numpy as np
import pickle
import ipdb
import json

def query_reddit(subreddit = None, from_date=None, until_date=None, search_query = None, size = 100):
    # TODO
    # Using PushShift API, scrape reddit comments related to {Bitcoin, Ethereum, Dogecoin, Cryptocurrency}
    # return a DataFrame of comments, columns should be 'body', 'created_utc', 'total_awards_received', 'subreddit'

    search_query_url = "https://api.pushshift.io/reddit/search/comment/?q=" + search_query + "&before=" + str(until_date) + "d&after=" + str(from_date) + "d&size=" + str(size)
    JSONDecodeError=True
    while JSONDecodeError == True:
        try:
            comments = requests.get(search_query_url).json()
            JSONDecodeError=False
            return comments
        except:
            pass

def clean_data(reddit_data: list, columns: list = None)-> list:
  # TODO
  # append comment lists to a new list, keeping elements that correspond to the passed in parameters
  pre_df = [columns]
  for comment in reddit_data:
      appending = []
      for column in columns:
          appending.append(comment[column])
      pre_df.append(appending)
  df = pd.DataFrame(data=pre_df[1:], columns=pre_df[0])
  return df

def main(filepath: str, query: str, date_range: int)-> None:
    """

    :param filepath:
    :param queries:
    :param column_names:
    :return:
    """

    # Import all data from reddit first
    # Store it in a list of dictionaries
    raw_reddit_query_data = [query_reddit(from_date=x+1, until_date=x, search_query=query)['data'] for x in range(date_range, 0, -1)] # list of daily_comments dict
    with open(query+".json", "w") as out_file:
        json.dump(raw_reddit_query_data, out_file, indent=4)
    # convert dictionaries to dataframe
    data_dict = {'text':[], 'date':[], 'score':[], 'awards':[]}
    for daily_comments in raw_reddit_query_data:
        for comment in daily_comments:
            data_dict['text'].append(comment['body']) if len(comment['body'])>0 else data_dict['text'].append('null')
            data_dict['date'].append(comment['created_utc']) if len(str(comment['created_utc']))>0 else data_dict['date'].append('null')
            data_dict['score'].append(comment['score']) if len(str(comment['score']))>0 else data_dict['score'].append('null')
            data_dict['awards'].append(comment['total_awards_received']) if len(str(comment['total_awards_received']))>0 else data_dict['awards'].append('null')
    df = pd.DataFrame(data_dict)
    df.to_csv(filepath, index=False)

if __name__ == "__main__":

    # filepath = "/home/alden/PycharmProjects/pythonProject/reddit_data_sets/"
    # queries = ["bitcoin", "dogecoin", "ethereum", "cryptocurrency", "economics", "finance", "politics", "election"]
    # column_names = ['body', 'created_utc', 'total_awards_received', 'subreddit']
    # IMPORTANT!! CURRENT DATE: 2/19/2022

    script, filepath, queries, date_range = sys.argv
    queries = queries.split()
    date_range = int(date_range)

    for query in queries:
        main(filepath+"reddit-"+query+".csv", query, date_range)
        
     
