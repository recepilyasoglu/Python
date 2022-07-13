# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("hw_25000.csv")

boy = data.Height.values.reshape(-1,1)
kilo = data.Weight.values.reshape(-1,1)
# -> boy ve kilo datası 25 bin tane x ve y için bana bir linefit et

# bu veriden yola çıkarak örneğin boy datasının kaç kiloya sahip olacağını tahminleyebiliyoruz
regression = LinearRegression()
regression.fit(boy,kilo)


print(regression.predict(np.array([[60]]))) # 60 boyda gelen bir kişi için kilo tahmini nedir? 
print(regression.predict(np.array([[62]])))
print(regression.predict(np.array([[64]])))
print(regression.predict(np.array([[66]])))
print(regression.predict(np.array([[68]])))
print(regression.predict(np.array([[70]])))


# print(data)
# print(data.columns)

#yukarda fit edilmiş line nın karşılığını grafikte çizgi çekerek verdi
plt.scatter(data.Height,data.Weight) 
x = np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red") # her x için x in karşılığı y yi predit edelim


plt.xlabel("Boy") # grafikte boy ve kilo yazmasını sağladık
plt.ylabel("Kilo")
plt.title("Simple Linear Regression Model")
plt.show()

#print(r2_score(kilo,regression.predict(boy))) 
# elindeki dataya bakarak benim sana verdiğim sonuç %25 doğruluk payına sahip 
# bunun 1 e ne kadar yakın olduğu çok önemli
# ve data fazlalığı da etkili bu data bu oran çok iyidir






