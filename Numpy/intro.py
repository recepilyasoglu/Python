# -*- coding: utf-8 -*-

import numpy as np

# havaDurumu = [[12,21,31],[6,17,18],[11,12,13]]
# print(havaDurumu)

a = np.arange(15).reshape(3,5) # 3 e 5 lik yapıyor verileri mesela 15 e kadar sayıları istedik sonra 3 e ayırdık gibi
print(a)
print(type(a))
print("Demension Count ="+str(a.ndim)) #boyut sayısını aldık

b = np.arange(10)
print(b.shape)
print(b.ndim)






