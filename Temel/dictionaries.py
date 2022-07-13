# -*- coding: utf-8 -*-

sozluk = {
     #key  :   value
    "book" : "kitap",
    "table" : "masa", 
    
    }

sozluk2 = dict(kitap ="book", masa="table") # bu şekilde de tanımlama yapılıyor


print(sozluk["book"]) #sozluk book'un değerini arattık

sozluk["book"] = "kitap1" #burda da değiştirdik değeri
sozluk["pencil"] = "kalem" #burda da değer ekledik
del(sozluk["book"]) #silme işlemi
print(sozluk)