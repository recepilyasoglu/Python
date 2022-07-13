# -*- coding: utf-8 -*-

sayilar = [1,2,3,4,5]

sayilarKareli = list(map(lambda sayi: sayi*sayi,sayilar)) #sayilardaki her biri sayi için sayinin karesini alıp listeye cevir sayilarkareliye aktar

# for sayi in sayilar:
#     sayilarKareli.append(sayi*sayi) # normal for la böyle yapılıyo


#filter
sayilarFiltreli = list(filter(lambda sayi: sayi>2,sayilar))# sayilardaki her bir sayi için 2 den büyük olması durumunda bunu listeye ekle demek

print(sayilarKareli)
print(sayilarFiltreli)

from functools import reduce
sayilarFaktoriyeli = reduce(lambda x,y: x*y, sayilar)
# x listedeki dizideki ilk sayıya takabül ediyo y de öteki sayıya mesela 
# x 1 ken y 2 çarp = 2 -> x artık 2 oldu, y de 3 aynı şekilde çarp = 6 -> x 6 oldu, y de 4 oldu

print(sayilarFaktoriyeli)



