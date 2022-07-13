# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["Last Name","First Name","SSN",
                  "Test1","Test4","Test4","Test4",
                  "Final","Grade"]
print(notlar)
print(notlar.head()) # en baştaki 5 datayı getirdi
print(notlar.tail()) # son 5 datayı getirdi

print(notlar["First Name"]) # burda data sıkıntılıydı yani bize gelen data "First name" olarak geldi
                            # sonra yukarda notlar.columns diyerek yeni değerler verdik
                            # !!! Bize gelen her data düzgün gelmeyebilir !!!
print(notlar["Grade"])
print(notlar.iloc[2])
print(notlar[1:5]) # 1 den 5 e kadar verileri istedik 5 dahil değil





