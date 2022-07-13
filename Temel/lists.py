# -*- coding: utf-8 -*-


#Lists
ogrenciler = ["Recep","Ahmet","Mücahit"]


print(ogrenciler[1])
ogrenciler.append("Ali") #listeye veri ekleme

ogrenciler.remove("Ahmet") #listeden veri silme

ogrenciler[1]="Hasan" #Mücahit'i değiştirdik Hasan oldu
print(ogrenciler)

#list constructor(liste oluşturucu)
sehirler = list(("Ankara","Istanbul"))
print(sehirler)

#print("Ankara Sayısı = "+ str(sehirler.clear())) #liste temizliyor
#print("Ankara İndexi = "+ str(sehirler.count("Ankara"))) #ankaranın sayısı kaç tane ankara var yani
#print(sehirler.pop(1)) #sehirlerden 1. elemanı çıkar demek
#print(sehirler.index(0,"İstanbul"))
sehirler.reverse() #tersten sıralama en baştaki sona, en sondaki en başa geliyor
print(sehirler)

sehirler3=sehirler.copy() #sehirlerin kopyasını kaydettik

#eşitleme
sehirler2=sehirler
sehirler2[0]="İzmir"

print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3) #sehirlere sehirler3'ü ekledik yani ekleme fonksiyonu extend
sehirler.sort() #alfabetik sıralama
sehirler.reverse() #tersten sıraladık
print(sehirler)
















