# -*- coding: utf-8 -*-
"""
@author: Anuj
"""

## Import packages
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

## Import data
csv_file = 'C:/Users/Anuj/Desktop/Evolent Assessment/BeerData.csv'
beer_data = pd.read_csv(csv_file, encoding = "ISO-8859-1")

## Narrow down relevent columns
df = beer_data[['review_overall', 'review_time']]

## Convert time to UTC with year
df['review_time'] = df['review_time'].apply(lambda ts: datetime.datetime.utcfromtimestamp(ts).strftime('%Y'))

## Group by year of review and obtain average of overall rating within each year
g = df.groupby(["review_time"])
yearly_averages = g.aggregate({"review_overall":np.mean})

## Sort by overall average ratings from highest to lowest values
top_ratings = yearly_averages.sort_values(by='review_overall',ascending=False)

## Print year and ratings
print(top_ratings)
