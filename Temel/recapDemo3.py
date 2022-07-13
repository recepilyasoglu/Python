# -*- coding: utf-8 -*-
#asal sayi bulma
#asal sayilar 2,3,5,7,11,13

sayi = int(input("Sayiyi Giriniz...:"))

#for x in range(2,sayi):
   # if(sayi % x) == 0:
     #   print("Bu sayi asal değildir")
     #   break
    #if(sayi % x) == 1:
     #   print("Bu sayi asaldir")
       # break
    
asalMi = True
for x in range(2,sayi):
    if (sayi % x) == 0:
        asalMi = False
        break

if asalMi == True:
    print("Sayi Asaldir")
else:
    print("Sayi asal değildir")



