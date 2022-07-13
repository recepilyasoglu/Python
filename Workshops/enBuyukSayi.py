# -*- coding: utf-8 -*-

sayi1 = int(input("1. Sayiyi Giriniz...:"))
sayi2 = int(input("2. Sayiyi Giriniz...:"))
sayi3 = int(input("3. Saayiyi Giriniz..:"))

if (sayi1>sayi2) and (sayi1>sayi3):
        print("Girdiğiniz " +str(sayi1)," sayisi en büyük sayi")
        
if (sayi2>sayi1) and (sayi2>sayi3):
        print("Girdiğiniz " +str(sayi2)," sayisi en büyük sayi")
        
else:
        print("Girdiğiniz " +str(sayi3)," sayisi en büyük sayi")

