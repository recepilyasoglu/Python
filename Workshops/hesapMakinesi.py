# -*- coding: utf-8 -*-

def Topla(sayi1,sayi2):
    return sayi1 + sayi2

def Cikar(sayi1,sayi2):
    return sayi1 - sayi2

def Carp(sayi1,sayi2):
    return sayi1 * sayi2

def Bol(sayi1,sayi2):
    return sayi1 / sayi2

print("-------Hesap Makinesine Hoş Geldiniz-------")

print("---Dört İşem Mevcuttur---")

print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")

secenek = int(input("Yapılacak İşlemi Seçiniz..:"))

if secenek > 4:
    print("Girmiş Olduğunuz Seçenek Şıklar Arasında Almamaktadır!!!")
    raise SystemExit
    
sayi1 = int(input("1. Sayiyi Giriniz...:"))
sayi2 = int(input("2. Sayiyi Giriniz...:"))


if secenek == 1:
    print(str(sayi1)+ " + " +str(sayi2)+" Sonucu...:" + str(Topla(sayi1, sayi2)))   
elif secenek == 2:
    print(str(sayi1)+ " - " +str(sayi2)+" Sonucu...:" + str(Cikar(sayi1, sayi2)))   
elif secenek == 3:
    print(str(sayi1)+ " * " +str(sayi2)+" Sonucu...:" + str(Carp(sayi1, sayi2)))    
elif secenek == 4:
    print(str(sayi1)+ " / " +str(sayi2)+" Sonucu...:" + str(Bol(sayi1, sayi2)))











