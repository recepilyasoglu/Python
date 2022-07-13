# -*- coding: utf-8 -*-

import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

c = a-b
d = b**3
e = 10 * np.sin(a)
 
print(e<7) # e deki tüm elamanlar 7 den küçük mü?
print(a*b)
print(a@b) # matris çarpımını veriyor

f = np.ones((2,4)) # 2 ye 4 lik 1 lerden oluşan matris
g = np.zeros((2,4)) # 2 ye 4 lük 0 lardan oluşan matris
h = np.random.random((2,4)) # rastgele sayılar üret
i = np.sum(b) # topladı b dekileri
j = np.min(b) # b deki en küçük değer
print(j)
l = np.sqrt(b) # kareköklerini aldık
print(l)





