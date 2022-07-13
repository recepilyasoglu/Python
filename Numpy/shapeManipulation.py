# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((3,4))) # 3e 4 lük rastgele array üret
b = np.floor(20*np.random.random((4,5)))


print(a)
print(a.shape) # dizi yapısı
print(b)
print(a.ravel()) # dizeyidüzlüyor
print(a.T) # transpozunu alıyor