# -*- coding: utf-8 -*-

from random import randint

rand = randint(1,100)
sayac = 0

while True:
    sayac+=1
    sayi = int(input("1 ile 100 arasinda bir sayi giriniz (0 çıkış)..:"))
    if sayi==0:
        print("Oyundan Çıkış Yapmak İstediniz :( ")
        break
    if sayi<rand:
        print("Daha Küçük Sayi Girmeyi Dene :)")
        continue
    if sayi>rand:
        print("Daha Büyük Sayi Girmeyi Dene :)")
        continue
    else:
        print("Rastgele Seçilen Sayi {0}!".format(rand))
        print("Tahmin Sayiniz {0}".format(sayac))












