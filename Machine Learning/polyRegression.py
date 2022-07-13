# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures # polinom özelliklerini import et


data = pd.read_csv("positions.csv")
print(data.columns)

# amaç = level yükseldikçe maaşın yükseldiğini gözlemlemek

# x i yakalamaya çalışıyoruz
level = data.iloc[:,1].values.reshape(-1,1) # sklearn bunu bizden istiyor  
# y yi yakalamaya çalışıyoruz
salary = data.iloc[:,2].values.reshape(-1,1)

regression = LinearRegression()
regression.fit(level,salary)

tahmin = regression.predict(np.array([[8.3]])) # mesleki seviyesi 8,3 olan kişi yıllık ne kadar maaş alır  


regressionPoly = PolynomialFeatures(degree = 4)
levelPoly = regressionPoly.fit_transform(level) # benim elimde level değerleri var sen onu polinom görüntü haline getir demek   
regression2 = LinearRegression() # yeni linear regression oluşturuyoruz ama bunu yeni x e göre yapıyoruz, çünkü yukarda x in yapısını değiştirdik
regression2.fit(levelPoly, salary)

tahmin2 = regression2.predict(regressionPoly.fit_transform(np.array([[8.3]]))) # tekrardan fit etmemiz gerekti hata aldığımız için

plt.scatter(level, salary, color="red")
plt.plot(level, regression.predict(level),color="blue") # her lecel için çizgi çizecek yani      
plt.plot(level, regression.predict(levelPoly))# regression2 yi levelPolylerin tamamı için uygula
plt.show()
 


