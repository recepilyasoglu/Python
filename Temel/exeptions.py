# -*- coding: utf-8 -*-

try: 
    sayi = int(input("Sayi Giriniz..:"))
except ValueError:
    print("Tip Uyuşmazlığı : Lütfen Sayı Giriniz!!!") # eğer bu hatayı alırsan
except ZeroDivisionError:
    print("Payda Sıfır Olamaz!!!")
except:
    print("Bir Hata Oluştu!!!")

print("Bitti")

