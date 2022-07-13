# -*- coding: utf-8 -*-

#SET UNION
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB) #Bu Union'lama işlemi 4'ü birden fazla kez yazmadı mesela ortak olanları bir defa yazıyor yani  
print(setA.union(setB)) #böyle de yazılabiliyor fonksiyon halinde yazdık burada
print(setB.union(setA)) #tam tersini de yapabiliyoruz tabi Union'un olayı bu yani


#SET İNTERSECTİON(kesişim)

print(setA & setB) #sadece burda ve(&) operaötü atıyoruz kesişenleri alıyor, iki listede olanları yani
print(setA.intersection(setB)) #bunlar fonksiyon hali yukardaki gibi
print(setB.intersection(setA))


#SET DİFFERENCE(fark)

print(setA - setB) 
print(setA.difference(setB)) #A fark B yani A da olan B de olmayan yukadakiyle aynı iş, bu onun sadece fonksiyon hali  
print(setB.difference(setA)) #B de olan A da olmayan

#SYMMETRİC DİFFERENCE(simetrik fark)

print(setA ^ setB) #shift+3 sonra da space yapınca çıkıyor
print(setA.symmetric_difference(setB)) #Birbirlerinde olmayanları yazıyor A da olup B de olmayanlarla, B de olup A da olmayanları bir yerde yazıyor
print(setB.symmetric_difference(setA))



