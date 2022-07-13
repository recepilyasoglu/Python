# -*- coding: utf-8 -*-

#eldeki verileri soyaya yazmak

ogrenciler = ["Recep","Mücahit","Ahmet"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")

fileToAppend.close()












