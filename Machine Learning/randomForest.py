# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("positions.csv") 
level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values  # sklearnin istediği veri tipiyle alakalı, y yi tek boyutlu istediği için reshape kısmını burdan sildik hata alıyorduk çünkü

# regression = RandomForestRegressor(n_estimators=10) # kaç tane decision tree oluşturayım sorusunun cevabı bu 5 tane yani istersen 1000 tane koayabilirsin dataya bağlı  
regression = RandomForestRegressor(n_estimators=10, random_state=2) # her seferinde farklı sonuç  almayalım diye random state ekledik
regression.fit(level, salary)


print(regression.predict(np.array([[8.3]])))


