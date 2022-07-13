# -*- coding: utf-8 -*-

#Substring
message= "Merhaba Dünya"
print(message[2:5])  #2 den 5 e kadar harfleri yaz

yeniMesaj = message[2:5] #2. harften itibaren hepsini yaz

#len
print(len(message))  #metnin uzunluğunu aldık

#lower, upper

print(message.upper())
print(message.lower())

#replace
print(message.replace("ü", "u")) #ü yü u ya cevirdik önce eski hali sonra yeni hali
print(message.replace ("a", "e"))

#split kelRime olarak parçalarına ayırıyor, sprit de boşlukları kaldırıyor
bilgi="Recep;İlyasoğlu;22;Bursa"
print(bilgi.split())
print(bilgi.split(";")) #virgüle göre ayırdı
print("Adı=" +bilgi.split(";")[0]) #Adı=Recep yazdırdık

#input kulanıcıdan veri almaya yarıyor
ad = input("Adınız?") #adını girdikten sonra sağ ekranda ad yazığında Recep yazıyor o da var

sayi1 = input("Sayi1?")
sayi2 = input("Sayi2?")
print(int(sayi1) + int(sayi2))















































































