# -*- coding: utf-8 -*-


import sqlite3

connection = sqlite3.connect("ddl.db")

cursor = connection.cursor()

def tabloOlustur():
    cursor.execute("""CREATE TABLE dwh
                   (customer_id NUMERIC,user_id NUMERIC, first_name VARCHAR(100) ,last_name VARCHAR(100),
                    door_number VARCHAR(30), street VARCHAR(200), postal_code VARCHAR(20), 
                    city VARCHAR(100), state_code VARCHAR(30),country VARCHAR(100), 
                    address_description TEXT,
                    msisdn_number VARCHAR(100), subscription_start_date TIMESTAMP, 
                    subscription_end_date TIMESTAMP, imsi VARCHAR(100), imei VARCHAR(100),
                    service_type TEXT, start_datetime TIMESTAMP, end_datetime TIMESTAMP, quantity INT8,
                    unit_of_quantity VARCHAR(40),destination_number, serving_cell_address VARCHAR(250), 
                    gdr_id INT8,call_type VARCHAR(32), extbillingaccountid INT8, cdate DATE, etl_date TIMESTAMPTZ)                   
                   """)

    connection.commit()
    connection.close()
        

tabloOlustur()