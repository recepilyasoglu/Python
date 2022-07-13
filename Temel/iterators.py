# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir"]

iteratorum = iter(sehirler)

print(next(iteratorum))# sırasıyla geziyor 2.nextte ikinci veriye gidiyor
print(next(iteratorum))
print(next(iteratorum))

#☻ yukardakinin yaptığı işi forla da yapıyoruz
for sehir in sehirler:
    print(sehir)











