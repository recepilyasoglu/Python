# -*- coding: utf-8 -*-


tupleListe = (2,4,6,"Ankara",(2,3,4),[]) #eleman sayısı 5 oldu
liste = [2,4,6,"Ankara",[3,4,5],[]] # aynı şekilde de burda da eleman sayısı 5 oldu

print(type(tupleListe)) #listeerin tiplerini aldık
print(type(liste))

tupleDeger=("Recep",) #normalde Recep yazdığımızda tip olrak str çıkardı türünü, ama sonuna virgül atınca tuple olarak çalıştı tuple olarak algıladı yani
print(type(tupleDeger))

print(tupleListe[1:2]) #1. indexten 2. indexe kadar olan veriyi yazdık yani 4 ama tuple da hemen yanına virgül atıyor
print(liste[1:2]) #burda normal 4 yazdı 1. index den 2. index'e kadar olan eleman

print(tupleListe[-2]) #listedeki elemanlardan en sağdan 2.yi yazdırdı (2,3,4)'ü
print(liste[-2]) #aynı şekil burda da [3,4,5]'i yazdırdık



print(tupleListe) 
print(liste)

print(len(tupleListe)) #burda da görüldüğü gibi 5 eleman 
print(len(liste))





