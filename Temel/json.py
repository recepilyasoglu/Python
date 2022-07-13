# -*- coding: utf-8 -*-

import json

data = '{"firstName":"recep","lastName":"ilyasoglu"}'

y = json.loads(data) # json formatındaki stringi, jsona çevirdik

print(y["firstName"])
print(y["lastName"])

customer = {   
            "firstName":"Recep",
            "email":"rcp.ilyasoglu@gmail.com"
            }

customerJson = json.dumps(customer) # pyton verisi çevirdik
print(customer)

print(json.dumps("Recep")) # stringi jsona çevirdk




