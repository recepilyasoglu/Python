# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10)

print(a)

b = a
print(b)
print(a[2])
print(b[2])

b[0]=100

print(a)
print(b)

c = a.copy() # c ye a'nın kopyasını attık c de yapılan değişikler a ya yansımaz çünkü ikiside artık farklı adresleri göstriyor her ne kadar aynı veriler olsa da 
print(c)
c[0]=1000
print(a) # burda da değişmediğini gördük ama yukarda b de değişmişti çünkü orda ikisi ayn ı adersi gösteriyodu
print(c) # yani yukarda b de yapılan değişiklikler aslında dreste yapılıyor onun için a da değişiyodu
         # ama burda c de yapılanlar a nın kopyasını tuttuğu için sadece c de değişiklik yapmış oluyoruz bu çok önemli!!!!

d = a.view() # ikisinde de data değişiyor
print("***")
print(a)
print(d)
d[0]=250
print(a)
print(d)
d.shape = 2,5
print(a)
print(d)
a[0]=123
print(a)
print(d)
