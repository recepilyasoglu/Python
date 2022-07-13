# -*- coding: utf-8 -*-
# 03/09/2021 05:04 ezan okucak az sonra devamkee inşallah etiya olur hayırlısıysa iş olarak çok sıkıldım çünkü yeter düzenli hayatım olsuun
import pandas as pd

orders = pd.read_table('orders.tsv')

print(orders.head())
print(orders.columns)
orders.item_name = orders.item_name.str.upper() # item nameleri büyüttük string operasyonuyla
print(orders.item_name)
print(orders.item_name.str.contains('Chicken'.upper())) # hangi datalarda chicken olduğuna baktık
orders.choice_description = orders.choice_description.str.replace('[','').str.replace(']','') # kapalı parantezi kaldırıp yerine boşluk attık bişey olmasın dedik yani replace ona yarıyore


