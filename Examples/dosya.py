# -*- coding: utf-8 -*-

f = open("musteriler.txt") # w write dan geliyor dosyayı oluşturmak, r de Read yani okumak default olarak belirtmek gerekir
                               # a da append yani yeni eklemeler yapıyor, x de create yani oluşturmak         

#print(f.read()) # tamamını okuyor

print("********")

#print(f.readline()) # satır satır okumak

for l in f: # dosyadaki bütün line ları gez satırları gez yani
    print(l)

fileToAppend = open("ogrenciler.txt","a") #w de dosyanın üzerine yazıyoruz yani var veri gidiyor onun için  "a" -create
fileToAppend.write("\n") # enter atıyoruz yoksa yan yana yazıyor isimleri txt ye
fileToAppend.write("Recep")
fileToAppend.close()

#%%
#import os 
#os.remove("ogrenciler.txt") # dosyayı siliyoruz

import os
if os.path.exists("ogrenciler.txt"): # ogrencilr.txt var mı ? varsa remove etsin
    os.remove("ogrenciler.txt")
else:
    print("Dosya yok")

os.rmdir("empty") # dosyayı siliyor







