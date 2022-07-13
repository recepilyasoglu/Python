# -*- coding: utf-8 -*-

import pandas as pd 

notlar = pd.read_csv("grades.csv")
notlar.columns=["Last Name","First Name","SSN",
                "Text1","Text2","Text3","Text4",
                "Final","Grade"]

print(notlar)
print(notlar.loc[:,"First Name"]) # bana bütün isim kolonunu ver
print(notlar.loc[:5,"First Name"]) # ilk 5 ismi ver 5 dahil
print(notlar.loc[:5,"First Name":"Text4"]) #ilk 6 satırı ve kolonlardan da Test4 e kadar olanı getirdi
print(notlar.loc[:5,["First Name","Last Name","Grade"]]) # 5.indexe kadar ki ve First Name ile Final(Grade) notunu 
print(notlar.loc[:5,:"Text2"]) # en baştan text2 ye kadarki herşeyi getirdi, (":" işareti en baştan itibaren demek yani;)    
print(notlar.loc[::-1,:"First Name"]) # tersten itibaren getir -> "::-1" bu işaret getirtiyor





