# -*- coding: utf-8 -*-

# sayi = int(input("Faktoriyeli Hesaplanacak Sayiyi Griniz..:"))

# faktoriyel = 1

# if sayi<0:
#     print("Negatif Sayilarin Faktoriyeli Hesaplanamaz")
    
# elif sayi==0:
#     print("Sonuc : 1")    

# else:
#     for i in range(1,sayi+1):#girilen sayiya kadar olduğu için +1 ekliyoruz
#         faktoriyel = faktoriyel * i
        
#     print("Sonuç..:",faktoriyel)

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())











