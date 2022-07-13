# -*- coding: utf-8 -*-

import pandas as pd 

data1 = {
            'id':[1,2,3,4],
            'adi':["Recep","Mücahit","Ahmet","Muharrem"],
            'soyadi':["İlyasoglu","Çelikbalta","Gören","Ünlütekin"]  
        }

data2 = {
            'id':[1,3,4,7],
            'adi':["Elif","Ali","Mehmet","Muzaffer"],
            'soyadi':["İlyasoglu","Çelikbalta","Gören","Ünlütekin"]  
        }

data1Df = pd.DataFrame(data1) 
data2Df = pd.DataFrame(data2)

print(data1Df)
print(data2Df)

print(pd.merge(data1Df,data2Df,on='id',how='inner')) # id alanına göre join yani id si aynı olanlar yan yana getirecek
                                                     # iki tane datası id si aynı olanları yan yana getir yani -> "inner" eşleşenler gelir  
print(pd.merge(data1Df,data2Df, on='id',how='left')) # solda olup sağda olmayanları da getirir
                                                     # mesela e-ticaret sitesinde üye olup sipariş vermeyen müşterilere kampanya yapmak istemek
print(pd.merge(data1Df,data2Df, on='id',how='right'))# bu da sağda olup solda olmayanlar için

print(pd.concat([data1Df,data2Df])) # alt alta getirdi id ler sabit kalacak şekilde
print(pd.concat([data1Df,data2Df],axis=1)) # yan yana getirdi axis=1 le
