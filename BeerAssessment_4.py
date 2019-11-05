# -*- coding: utf-8 -*-
"""
@author: Anuj
"""

## Import packages
import pandas as pd
import numpy as np

## Import data
csv_file = 'C:/Users/Anuj/Desktop/Evolent Assessment/BeerData.csv'
beer_data = pd.read_csv(csv_file, encoding = "ISO-8859-1")

## Narrow down relevent columns
df = beer_data[['review_overall', 'review_taste','review_aroma','review_appearance','review_palette','beer_name']]
df['OverallAvgRating'] = df[['review_overall', 'review_taste','review_aroma','review_appearance','review_palette']].mean(axis=1)

## Group list by beer name and obtain overall average rating
g = df.groupby(["beer_name"])
Rating_averages = g.aggregate({"OverallAvgRating":np.mean})

## Sort by overall average rating from highest to lowest
top_beer = Rating_averages.sort_values(by='OverallAvgRating', ascending=False)

## Count number of reviews for each beer and 
## drop if there are less than 50 reviews
top_beer['num_reviews'] = df.groupby('beer_name')['beer_name'].size()
low_rate = top_beer[top_beer['num_reviews'] <= 50 ].index
top_beer.drop(low_rate , inplace=True)

## Print the top 10 beers
print(top_beer.head(10))
