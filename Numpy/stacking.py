# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((2,3))) # virgüllü sayı gelmesin diye floor attık
b = np.floor(10*np.random.random((2,3)))
print(a)
print(b)

c = np.vstack((a,b)) # 2 dizeyi alt alta yazdırdı
print(c)

d = np.hstack((a,b)) # 2 dizeyi yatay şekilde yazdırdı
print(d)


