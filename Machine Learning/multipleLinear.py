# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("insurance.csv")

print(data)
print(data.columns)

# harcamaları tahmin etmete çalışısyoruz onun için de elimizdeki datalardan yola çıkıcaz
# line fit edicez, bulucaz onun için de x ve y leri belirlememiz gerekiyor
# y için expensesi bulmaya çalışıyoruz birnevi
expenses = data.expenses.values.reshape(-1,1) # sk(sayki) nin formatına uygun hale getirmek için reshape yapıyoruz
# expensesi çektik yukarda, variable explorer dan bakabilirsn data geldi
## y eksenini oluşturduk

## x ekseni
# age ve bmi datalarını aşağıya doğru getirmek için iloc kullandık
ageBmis = data.iloc[:,[0,2]].values # 0 ve 1 deki tüm dataları al bunların valuelerini al

## bu arada bmi-> vücut kitle endeksi demek 

regression = LinearRegression()
regression.fit(ageBmis,expenses)

print(regression.predict(np.array([[20,20]]))) # 20 yaşında ve 20 vücut kitle endeksine sahip birinin harcaması
print(regression.predict(np.array([[20,21],[20,22],[20,23],[20,24]])))












