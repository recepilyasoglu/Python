# -*- coding: utf-8 -*-
import sys #nasıl bir hata olduğunu arka planda anlayabilmemiz için kullanıyoruz bu modülü

liste = [7,'Recep',6,3,"0"]

for x in liste: # listede geziyoruz
    try: 
        print("Sayı  :" + str(x))
        sonuc = 1/int(x)
        print(str(x)+" Sayısının 1'e Bölümüden Kalan Sonuç :" + str(sonuc))
    except ValueError:
        print(str(x)+" Sayi Değil!!")
    except ZeroDivisionError:
        print(str(x)+" Sıfıra Bölme Hatası!!!")
    except:
        print(str(x) +" Hesaplanamadı!!!")
        print("System Message : "+ str(sys.exc_info()[0]))
    finally:
        print("İşlemler Bitti") # hatalar olsun olmasın hertürlü yazar finally

 













