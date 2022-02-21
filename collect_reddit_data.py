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

def query_reddit(search_query=None, subreddit=None, from_date=None, until_date=None, size=100):

    search_query_url = "https://api.pushshift.io/reddit/search/comment/?q=" + search_query + "&subreddit=" + subreddit + "&before=" + str(until_date) + "d&after=" + str(from_date) + "d&size=" + str(size)
    JSONDecodeError=True
    print(from_date)
    count = 0
    while JSONDecodeError == True and count < 100:
        print("\t", count)
        count += 1
        try:
            comments = requests.get(search_query_url).json()
            JSONDecodeError=False
            return comments
        except:
            pass
    return {"data":[{"body":"null", "created_utc":"null", "score":"null", "total_awards_received":"null"}]}

def main(filepath: str, query: str, date_range: int)-> None:
    """

    :param filepath:
    :param queries:
    :param column_names:
    :return:
    """

    # Import all data from reddit first
    print("Collecting reddit data for: " + query + "\nStretching " + str(date_range) + " days back in time")

    raw_reddit_query_data = [query_reddit(search_query=query, subreddit=query, from_date=x+1, until_date=x)['data'] for x in range(date_range, 0, -1)] # list of daily_comments dict

    print("Done collecting " + query + " data.\nWriting to JSON file...")
    with open(filepath+query+".json", "w") as out_file:
        json.dump(raw_reddit_query_data, out_file, indent=4)

    print("Creating dictionary mappings...")
    data_dict = {'text':[], 'date':[], 'unix_time':[], 'score':[], 'num_awards':[]}
    for i, daily_comments in enumerate(raw_reddit_query_data):
        temp_date = date_range-i
        for comment in daily_comments:
            data_dict['text'].append(comment['body']) if len(comment['body'])>0 else data_dict['text'].append('null')
            data_dict['date'].append(temp_date)
            data_dict['unix_time'].append(comment['created_utc']) if len(str(comment['created_utc']))>0 else data_dict['unix_time'].append('null')
            data_dict['score'].append(comment['score']) if len(str(comment['score']))>0 else data_dict['score'].append('null')
            data_dict['num_awards'].append(comment['total_awards_received']) if len(str(comment['total_awards_received']))>0 else data_dict['num_awards'].append('null')
    df = pd.DataFrame(data_dict)

    print("Writing to csv...")
    df.to_csv(filepath+"reddit-"+query+".csv", index=False)
    print("Done!!\n\n\n")

if __name__ == "__main__":
    # IMPORTANT!! CURRENT DATE: 2/21/2022

    script, filepath, queries, date_range = sys.argv
    queries = queries.split()
    date_range = int(date_range)


    # collect all relevant data in one dataframe and store it as a csv
    # queries = [bitcoin, ethereum, dogecoin, cryptocurrency, economy, politics, finance, pandemic]
    for query in queries:
        main(filepath, query, date_range)

