#!/usr/bin/env python3

import pandas as pd

filename = 'data.csv'

def compute_price_variation(data):

    # read a CSV file into a DataFrame object
    dataframe = pd.read_csv(data, index_col=False, sep=";")

    # sort the dataframe by product (sku) and date
    dataframe = dataframe.sort_values(by=['product', 'activity_date'])

    # group the dataframe by product (sku) and take the last two dates
    last_two_dates = dataframe.groupby('product').tail(2)

    # calculate the price variation for each product (sku)
    price_variation = last_two_dates.groupby('product')['price'].apply(lambda x: x.iloc[-1] - x.iloc[-2]).reset_index()

    # rename the price variation column
    price_variation = price_variation.rename(columns={'price': 'price_variation'})

    return price_variation

if __name__ == "__main__":
    df = compute_price_variation(filename)
    # save the dataframe to a CSV file
    df.to_csv('product_price_variation.csv', index=False, sep=';')