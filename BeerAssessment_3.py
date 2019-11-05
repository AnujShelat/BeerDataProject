# -*- coding: utf-8 -*-
"""
@author: Anuj
"""

## Import packages
import pandas as pd

## Import data
csv_file = 'C:/Users/Anuj/Desktop/Evolent Assessment/BeerData.csv'
beer_data = pd.read_csv(csv_file, encoding = "ISO-8859-1")

## Narrow down relevent columns
df = beer_data[['review_overall', 'review_taste','review_aroma','review_appearance','review_palette']]

## Subtract each factor rating from the overall rating
dif_taste = df['review_taste'] - df['review_overall']
dif_aroma = df['review_aroma'] - df['review_overall']
dif_appearance = df['review_appearance'] - df['review_overall']
dif_palette = df['review_palette'] - df['review_overall']

## Add the absolute value of the difference in factor rating from overall rating
## to the overall rating
df['er_taste'] = abs(dif_taste) + df['review_overall']
df['er_aroma'] = abs(dif_aroma) + df['review_overall']
df['er_appearance'] = abs(dif_appearance) + df['review_overall']
df['er_palette'] = abs(dif_palette) + df['review_overall']

## Divide overall rating by the above value to obtain factor of importance
pdif_taste = df['review_overall']/df['er_taste']
pdif_aroma = df['review_overall']/df['er_aroma']
pdif_appearance = df['review_overall']/df['er_appearance']
pdif_palette = df['review_overall']/df['er_palette']

## Create new data frame with Importance values of each factor
df1 = pd.DataFrame(pdif_taste, columns = ['Importance of Taste']) 
df1['Importance of Aroma'] = pdif_aroma
df1['Importance of Appearance'] = pdif_appearance
df1['Importance of Palette'] = pdif_palette

## Display the average importance for each factor
print(df1.mean(axis=0))
