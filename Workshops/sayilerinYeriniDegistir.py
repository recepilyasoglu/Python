# -*- coding: utf-8 -*-

x = 10;
y = 20;


print("x = " + str(x))
print("y = " + str(y))

temp = x #geçici değer verip çözdük
x=y
y=temp

#veya

#x,y = y,x bu pythona özel

print("x = " + str(x))
print("y = " + str(y))














