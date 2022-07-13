# -*- coding: utf-8 -*-

def selamVer(isim): #fonksiyon tanımlama
    print("Merhaba " +isim )
    
selamVer("Recep")


def selamVer2(isim=" ziyaretçi"): #default parametreli fonksiyon yani isim vermezsen default olarak atadığın değeri yazdırır
    print("Merhaba "+isim)
    
selamVer2()


def selamVer3(isim=" ziyaretçi", soyIsim= " arkadaş"):#default değerleri parantezin en sonuna saklamak gerekir
    print("Merhaba " +isim + " " + soyIsim)

selamVer3("Recep","İlyasoğlu")


#değer return eden fonksiyonlar
def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2,3)

print(alan)

#lambda fonksiyonlar

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2))

#bu tarz atama da yapılabiliyor

x = dikUcgenAlaniHesapla2

print(x(4,5))






