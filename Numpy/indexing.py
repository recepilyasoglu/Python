# -*- coding: utf-8 -*-

import numpy as np

sayilar = np.array([0,5,10,15,20,25,30])

print(sayilar[4])
print(sayilar[0:3])
print(sayilar[::-1]) # diziyi tersten ver 

sayilar2 = np.array([[0,5,10],[15,20,25]])
print(sayilar2[0])
print(sayilar2[1,2]) # 1. satırın 2. indexini ver
print(sayilar2[:,2]) # tüm satırlardan 2. idexi ver





