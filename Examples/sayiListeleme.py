# -*- coding: utf-8 -*-

sayilar = [15,25,40,92,65,35,20,16]
sayac = 0
for i in sayilar:
    if i%5==0:
        print(str(i)+" Sayisi 5'in Katıdır")
        sayac = sayac+1
else:
   print("Döngü Bitti")

print("5'in Kati Olan Sayi Adeti..:"+str(sayac))
