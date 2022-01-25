"""
collect_reddit_data.py
a python script for collecting ethereum, dogecoin, and bitcoin related posts from reddit

Usage: collect_reddit_data.py <start_date> <end_date> <output_filename>
Example: python3 collect_reddit_data.py 01-01-2016 01-01-2022 "reddit_data.csv"
"""

# need to "pip install praw" before running if not already installed

import sys
import numpy as np
import pandas as pd
import praw

script, start_date, end_date, output_filename = sys.argv

main(start, end, out_file):
  
  # TODO Use Reddit API to collect Historical text data related to Cryptocurrencies
  # search in r/bitcoin, r/ethereum, r/dogecoin, r/cryptocurrency
  # Export data to CSV: Columns: [date, text, upvotes, awards], each row contains one post

  
  df.to_csv()
  
if __name__ == "__main__":
  
  main(start_date, end_date, output_filename)
