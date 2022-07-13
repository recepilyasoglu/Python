# -*- coding: utf-8 -*-

import pandas as pd # iki modülle çalışıyoruz
import numpy as np
 
data = np.array(["Recep","Mücahit","Ahmet","Muharrem"])
s = pd.Series(data, index=[1,2,3,4]) # index vermeden önce 0 dan başlatıyo index vererek bu sayılardan başla dedik bir nevi


data2 = {"matematik": 10,"fizik" : 20,"beden eğitimi":100}
s2 = pd.Series(data2) # yukarda sözlükte tanımlamalar yaptığımız içi extra index vermiyoruz istersen verebilirsin tabi yine de
print(s2)

print(s2[0])
 
s3 = pd.Series(5,index = [1,2,3,4,5])
print(s3)








