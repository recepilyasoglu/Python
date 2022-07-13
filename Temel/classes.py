# -*- coding: utf-8 -*-

class Matematik:
    def topla(self,sayi1,sayi2): #aşağıda matematik diye nesne oluşturduk ya onun kullanabilmesi çin self vermemiz gerekiyor ona denk geliyor
        return sayi1+sayi2 #classın referansına denk geliyor self
    
    def cikar(self,sayi1,sayi2):
        return sayi1-sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1*sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1/sayi2
    
matematik = Matematik() #bellekte matematik diye nesne oluşuyor
print("Toplam = " + str(matematik.topla(2,78)))

#%% Property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Recep","İlyasoğlu",23)
print(person1.firstName)
print(person1.lastName)
print(person1.age)

#miras alma 
class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
ahmet = Worker()

mehmet = Customer()






















