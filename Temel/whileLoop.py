# -*- coding: utf-8 -*-
sayac = 1
sonuc = 0

while sayac <= 10:
    sonuc = sonuc + sayac
    sayac = sayac + 1
    
print(sonuc)


#Range fonksiyonu
for x  in range(100): # 100 e kadar saydırma
    print(x+1) # 1 den başlattık

for x in range(1,10,2): #1 den 10 a kadar tek sayıları yazdırır
    print(x)

for x in range(2,10,2): # 1 den 10 a kadar çit sayıları yazdırır
    print(x)