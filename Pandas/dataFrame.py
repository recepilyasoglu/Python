# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = [10,20,30,40]
df = pd.DataFrame(data) # bunun series den farkı hem index hem kolon değerlerini veriyor
print(df)

data2 = ["Recep",23,"Tetovo"],["Ahmet",23,"Roma"],["Mücahit",23,"Bursa"]
df2 = pd.DataFrame(data2, columns=["İsim","Yaş","Şehir"], index=[1,2,3])# columns(kolonlar) da yine index no lar vardı değiştirdik onları
print(df2)

data3 = {"İsim" :["Recep","Ahmet","Mücahit"],
         "Yaş":[23,23,23],
         "Şehir" :["Tetovo","Roma","Bursa"]}
df3 = pd.DataFrame(data3, columns=["İsim","Yaş","Şehir"], index=[1,2,3])# columns(kolonlar) da yine index no lar vardı değiştirdik onları
print(df3)
# df3.pop("Şehir") # şehir kolonunu sildik uçurduk yani
# print(df3)

print(df3.loc[2])
print(df3.iloc[1]) # integer loc yani sırada ilk kim geliyosa 0.index dışında alıyor ilk değeri yani ahmeti

df4 = df3.append(df2) # iki veriyi bir araya getirdik
print(df4) 
print(df4.head()) # en tepedeki datayı getirir
print(df4.tail()) # sondaki datayı verir


# def power(x, y):
#   if y == 0:
#     return 1
#   else:
#     return x * power(x, y-1)
# 		
# print(power(2, 3))

# def spell(txt):
#     #your code goes here
#     if txt=="": 
#         return txt
#     else:
#         print(txt[len(txt)-1])
#         return spell(txt[0:len(txt)-1])

# weight = int(input("weight :"))
# height = float(input("height :")) 

# bmi = weight / float( height**2 )

# if (bmi < 18.5) :
#     print("Underweight")

# elif bmi >= 18.5 and bmi < 25 :
#     print("Normal")
    
# elif bmi > 25 and bmi < 30:
#     print("Overweight")

# elif bmi > 30 :
#     print("Obesity")
    
    
    
    
    
a = 2
b = 2
a = a + b
b = 2 * a 
a = a + a 


print("a : ",a)
print("b : ",b)


x2 = [i+3 if i<2 else i for i in range(3)]
print(x2)



reco = True + True and False + (True + False and True + False) ** 5

print(reco)

reco2= "Rishu"

print(reco2[0::-1].replace("R","r"))

sxs = (5 * 2 + 7 -20 / 2) ** 2

print(sxs)

sxs2 = 1/2 * (( -2 * (2 + 3) * 20) // 2)

print(sxs2)

print('abcdefcdgh'. partition('cd')) 

sxs3 = [x for x in range(1000) if x%3==0]

print(sxs3)

a = "BTK Akademi"

print(a.index("B"))

meyve = "elma"

print(type(meyve))

sayac=0 
sayi=input('Sayı:') 
for i in range(2,int(sayi)): 
    if(int(sayi)%i==0): 
        sayac+=1 
        break 
    if(sayac!=0): 
        print("&&&&&") 
    else: 
        print("#####") 
        
numpy_array=np.array([0,1,2,3,4,5]) 

print(numpy_array.reshape(2,3)
