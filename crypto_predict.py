# TODO: Using historical sentiment metrics and cryptocurrency data, 
# Train a machine learning model to attempt to predict long term changes in Crypto prices

import numpy
import pandas
import torch

# We will use a LSTM from torch library
# It will take in the previous 30 days of crypto data (high, low, close, volume, cap)
# It will also take in ...
# Hyperparameter selection

def main(data: pd.DataFrame):
  # TODO create instance of machine learning model,
  # run the training, perform testing and then save
  
  
def train():
  # train the model using the library's built in functionality
  
def test():
  # test the model using the library's built in functionality
  
  
if __name__ == "__main__":
  
  filename = "final_data.csv"
  df = pd.read_csv(filename)
  
  main(df)
