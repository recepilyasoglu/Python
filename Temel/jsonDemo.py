# -*- coding: utf-8 -*-

import json

with open("users.json") as users:
    data = json.load(users)
    
    
    for x in range(6): # ilk 5 veriye ulaştık  
        #print(data[0]) # 0. veriye ulaştık yani ilk veriye
        print(data[x]["username"]) # username ulaştık
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        
        
        