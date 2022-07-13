# -*- coding: utf-8 -*-

import pandas as pd

films = pd.read_csv("imdb_1000.csv")

print(films)
print(films.columns)
print(films.head())
print(films.tail())
print(films[['title','star_rating']].head())
#print(films.title.head()) # yukardakiyle aynı iş 
print(films[:9][['title','star_rating']].head())
print(films[films['star_rating']>8.5][['title','star_rating']]) # imdb 8.5 den büyük olanları getirdi yani filtreledik
print(films[
    (films['star_rating']>8.5)&(films['star_rating']<9.0)
    ][['title','star_rating']])# imdb 8.5 den büyük 9.0 dan küçük olanları getirdi yani filtreledik
print(films[
    (films['star_rating']>=9.5)|(films['star_rating']<=7.4) #  veya attık
    ][['title','star_rating']])

print(films.query('star_rating>=9.0')) # birde  bu tarz filtreleme var
print(films.query('star_rating>=9.0 & star_rating<=9.3') # 9 dan büyük eşit ve 9.3 den küçük eşir filmleri getirdi
                  [['title','star_rating']])






