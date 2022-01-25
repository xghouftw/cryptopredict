"""
get_crypto_data.py
A short script for collecting crypto data related to
BTC, ETH, and DOGE from a pre-existing crypto csv file

Usage: get_crypto_data.py <filepath> <currencies>
Example: python3 get_crypto_data.py
"""

import pandas as pd

filepath = "/home/alden/PycharmProjects/ISEF/consolidated_coin_data.csv"
currencies = ["bitcoin", "ethereum"] # This dataset didn't contain doge for some reason

currencies = list(currencies)

print(type(currencies))

print(currencies)

def main(filepath, currencies):

    df = pd.read_csv(filepath)
    print("Displaying the contents of the csv file... \n", df.head(n=100), df.tail(n=100), "\n\n\n")

    for currency in currencies:
        df.loc[df['Currency'] == currency].to_csv(currency + "_data.csv")
        print(df.loc[df['Currency'] == currency])
    print("Done saving new data!\n\n\n")

    print("Done!")

if __name__ == "__main__":

    main(filepath, currencies)
