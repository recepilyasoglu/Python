# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("positions.csv")

level = data.iloc[:,1:2].values.reshape(-1,1) # inndex 1 den 2 ye kadar getir 2 yi dahil etme 
salary = data.iloc[:,2].values.reshape(-1.1)

regression = DecisionTreeRegressor()
regression.fit(level, salary)
print(regression.predict(np.array([[8.3]])))

plt.scatter(level, salary, color="red")
x = np.arange(min(level), max(level),0.01).reshape(-1, 1) # levelların minimumunu maximumunu al ve bunları küçük lüçük değerlerle çiz    
plt.plot(x, regression.predict(np.array(x)), color="orange").reshape(-1,1)
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Decision Tree Model")

plt.show()



