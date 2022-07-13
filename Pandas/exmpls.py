# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv("grades.csv")
                   
print(data.to_string())

print(data.columns)

print(data.head())

print(data.tail())

print(data.info())