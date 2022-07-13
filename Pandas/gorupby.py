# -*- coding: utf-8 -*-

import pandas as pd 

films = pd.read_csv("imdb_1000.csv")

print(films.columns)
print(films.head())
print(films.star_rating.mean()) # ilk 1000 filmin ortalama puanı

print(films.groupby('genre').star_rating.mean()) # filmin her türü için ortalama al, en beğeni alan kategorilere baktık
                    
                











