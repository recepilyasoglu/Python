# -*- coding: utf-8 -*-

import sqlite3

def selectOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    
    #cursor = connection.execute("select * from customers")
    
    #for row in cursor:
    #   print("CustomerID = "+str(row[0])+" First Name = "+row[1]+" Last Name = "+row[2])
       
    
    #cursor = connection.execute("select FirstName,LastName from customers where city='Prague' or city='Berlin'")
    #prague sehirli olanları getirdi veya berlinlileri
    # for row in cursor:
     #   print("First Name = "+row[0])
     #   print(" Last Name = "+row[1])
      #  print("**********")
    
    
    # cursor = connection.execute("""select FirstName,LastName 
    #                             from customers 
    #                             where city='Prague' or city='Berlin'
    #                             order by FirstName""") # 0rder by alfabetik sıraya göre FirstName'leri sıraladık
    
    # for row in cursor:
    #     print("First Name = "+row[0])
    #     print(" Last Name = "+row[1]) 
    #     print("**********")
    
    # cursor = connection.execute("""select city,count(*) from customers 
    #                             group by city having count(*)>1 
    #                             order by count(*) desc""") # müşteri sayısı azalan şekilde (desc yani)
    #                             # 1 den fazla müşterileri şehire göre getir
    # for row in cursor:
    #     print("City = "+row[0])
    #     print("Count = "+str(row[1]))
    #     print("**********")
    
    cursor = connection.execute("""select FirstName,LastName 
                                from customers 
                                where FirstName like '%a%' """)  #isminin içerisinde a olanları getir like operatörü yani
                                # a% -> a ile başlayanlar, %a -> ile bitenler, %ad -> ile bitenler
    for row in cursor:
        print("First Name = "+row[0])
        print(" Last Name = "+row[1]) 
        print("**********")

 
    connection.close()
    
selectOperasyonlari()

def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                       (firstName,lastName,city,email)
                       values('Recep','İlyasoğlu','Bursa','rcp.ilyasoglu@gmail.com')""")
    connection.commit()
    connection.close()
                  
#insertCustomer()   


def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city ='İstanbul'  
                       where city ='Bursa'""")
    connection.commit()
    connection.close()

#updateCustomer()

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers 
                       where city='İstanbul'""")
    connection.commit()
    connection.close()

#deleteCustomer()                   



def joınOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select albums.Title, artists.Name from artists inner join albums
                             on artists.ArtistId = albums.ArtistId
                             """)  #isminin içerisinde a olanları getir like operatörü yani
                                # a% -> a ile başlayanlar, %a -> ile bitenler, %ad -> ile bitenler
    for row in cursor:
        print(" Title = "+row[0]+" ------ Name = "+row[1])
       

 
    connection.close()
    
joınOperasyonlari()
    
