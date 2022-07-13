# -*- coding: utf-8 -*-


import pandas as pd

readData = pd.read_csv("imdb_1000.csv")

print(readData)
print(readData.columns)
print(readData.head())
print(readData.title.head())
print(readData[['title','star_rating']].head())

print(readData[
    (readData['star_rating']>=8.5) & 
               (readData['star_rating']<=9.5)]
              [['title','star_rating']])







