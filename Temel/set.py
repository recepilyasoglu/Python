# -*- coding: utf-8 -*-

studentsSet = {"Recep","Ahmet","Mücahit"}
print(studentsSet) #yazdırdığımızda sırayla gelmedi çümkü indexsiz, sırasız listeleme ve çok hızlı çalışıyor

for student in studentsSet:
    print(student) #döngü kurup elemanlara ulaştık
    
    
print("Ahmet" in studentsSet) #true yada false olarak döndürüyor true var false yok büyük-küçük harf duyarlılvar pythonda onun için yazarken listedeki yazmak gerekir

if "Ahmet" in studentsSet:
    print("Listede Var") #burda da if atıp varsa yani true'sa "Listede Var" yazdırdık 
    

#LİSTEDE ELEMAN DEĞİŞTİREMİYORUZ AMA ELEMAN EKLEYEBİLİYORUZ     
studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Merve","Mert","Selin"])
print(studentsSet) #update ettik direk seti update'ledik yani
print(len(studentsSet))

studentsSet.remove("Selin") #seçili elemanı sildik 
print(studentsSet) 


studentsSet.discard("Selin")
print(studentsSet) #burda hata verir iki defa eleman silmeye çalıştığımız için ardında remove'u discard yaparsak hata ortadan kalkar
print(len(studentsSet))

x = studentsSet.pop() #listeden son elemanı silmeye yarıyor
print(len(studentsSet))
print(studentsSet)

 



