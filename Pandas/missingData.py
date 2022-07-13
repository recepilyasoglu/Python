# -*- coding: utf-8 -*-

import pandas as pd 

url = "http://bit.ly/uforeports" # url tanımladık

data = pd.read_csv(url) # burda da okuttuk

print(data)
print(data[["City",
            "Colors Reported",
            "Shape Reported",
            "State",
            "Time"]].head())
print(data.columns)
print(data.isnull().head(100)) # bana ilk 100 data için null değerleri göster colors reported null dı ya yani boş mu diye soruyor true veya false alarak cevabı öğreniyoruzz  
print(data.notnull().head(100)) # burda da boş değil mi ? sorusu evet boş değil veya hayı boş gibi 
print(data.isnull().sum()) # isnulların toplamını ver yani boş alanların adedi
print(data[data.City.isnull()]) # city bilgileri için isnull olanları bana göster

#dropna
print(data.shape) # adet veri bilgisi
#data = data.dropna(how = "any") # drop edeyim ama nasıl? -> any yani herhangi bir satırın herhangi bir değeri null ise onu uçurr !!!
#data = data.dropna(how = "all") # herşeyin boş olduğu datamız yok onun için göremiyoruz
# data = data.dropna(
#     subset=['City','Colors Reported'],how='any') # şehirde olabilir colors reported da olabilir null olanı uçur

data['Shape Reported'].fillna(value='Belirsiz',inplace=True) # null olan datayı doldur demek ne olarak doldurayım? -> Belirsiz olarak doldur, değiştireyim mi? -> inplace=True evet değiştir 
print(data['Shape Reported'].value_counts(dropna=False)) # neye benzediği hakkında bilgi alıyoruz sayı alıyoruz

print(data.shape)








