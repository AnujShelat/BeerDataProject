# -*- coding: utf-8 -*-
"""
@author: Anuj
"""

## Import packages
from textblob import TextBlob
import pandas as pd
import numpy as np

## Import data
csv_file = 'C:/Users/Anuj/Desktop/Evolent Assessment/BeerData.csv'
beer_data = pd.read_csv(csv_file, encoding = "ISO-8859-1")

## Drop NA values
beer_data = beer_data.dropna(subset=['review_text'])

## Narrow down relevent columns
df = beer_data[['review_text','beer_style','review_overall']]

## Drop reviews below an overall rating of 4
low_rating = df[df['review_overall'] < 5 ].index
df.drop(low_rating , inplace=True)

reindexed_data = df['review_text']
reindexed_data.index = df['beer_style']

## Use TextBlob for sentiment analysis
blobs = [TextBlob(reindexed_data[i]) for i in range(reindexed_data.shape[0])]
polarity = [blob.polarity for blob in blobs]
df['polarity'] = polarity

## Make data frame for review text and sentiment
sentiment_analysed = pd.DataFrame({'review_text':reindexed_data,
                                   'polarity':polarity}, index=reindexed_data.index)

## Group list by beer name and obtain overall average polarity
g = df.groupby(["beer_style"])
polarity_averages = g.aggregate({"polarity":np.mean})

## Sort by overall average polarity from highest to lowest
top_beerstyle = polarity_averages.sort_values(by='polarity', ascending=False)

## Print beers with highest average polarity
print(top_beerstyle.head())