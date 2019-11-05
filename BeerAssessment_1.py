# -*- coding: utf-8 -*-
"""
@author: Anuj
"""

## Import packages
import pandas as pd

## Import data
csv_file = 'C:/Users/Anuj/Desktop/Evolent Assessment/BeerData.csv'
beer_data = pd.read_csv(csv_file, encoding = "ISO-8859-1")

## Drop NA values
beer_data = beer_data.dropna(subset=['beer_ABV'])

## Narrow down relevent columns
df = beer_data[['beer_brewerId', 'beer_ABV']]

## Sort by ABV from highest to lowest values
ABV = df.sort_values(by='beer_ABV', ascending=False)

## Print top 3 brewers with highest ABV values
print(ABV.drop_duplicates(subset='beer_brewerId', keep='first').head(3))
