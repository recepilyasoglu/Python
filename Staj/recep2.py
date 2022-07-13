# -*- coding: utf-8 -*-

import sqlite3

Create_SENSORLOG_Table = """CREATE TABLE IF NOT EXISTS recep2 (customer_id NUMERIC,user_id TEXT, first_name TEXT ,last_name TEXT,
                    door_number TEXT, street TEXT, postal_code TEXT, 
                    city TEXT, state_code TEXT,country TEXT, 
                    address_description TEXT,
                    msisdn_number TEXT, subscription_start_date TEXT, 
                    subscription_end_date TEXT, imsi TEXT, imei TEXT,
                    service_type TEXT, start_datetime TEXT, end_datetime TEXT, quantity TEXT,
                    unit_of_quantity TEXT,destination_number TEXT, serving_cell_address TEXT, 
                    gdr_id TEXT,call_type TEXT, extbillingaccountid TEXT, cdate TEXT, etl_date TEXT);"""

INSERT_SENSORLOG = "INSERT INTO recep2 (customer_id ,user_id ,first_name ,last_name ,door_number ,street ,postal_code ,city ,state_code ,country ,address_description ,msisdn_number ,subscription_start_date ,subscription_end_date ,imsi ,imei ,service_type ,start_datetime ,end_datetime ,quantity ,unit_of_quantity ,destination_number ,serving_cell_address ,gdr_id ,call_type ,extbillingaccountid ,cdate ,etl_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"


def connect():
    return sqlite3.connect("ddl2.db")

def create_tables(connection):
    with connection:
        connection.execute(Create_SENSORLOG_Table)

def add_sensorlog(connection, customer_id ,user_id , first_name ,last_name ,door_number ,street , postal_code ,city ,state_code ,country ,address_description , msisdn_number ,subscription_start_date ,subscription_end_date ,imsi ,imei , service_type ,start_datetime ,end_datetime ,quantity ,unit_of_quantity , destination_number ,serving_cell_address ,gdr_id ,call_type ,extbillingaccountid , cdate ,etl_date):
    with connection:
        connection.execute(INSERT_SENSORLOG,(customer_id ,user_id ,first_name ,last_name ,door_number ,street ,postal_code ,city ,state_code ,country ,address_description ,msisdn_number ,subscription_start_date ,subscription_end_date ,imsi ,imei ,service_type ,start_datetime ,end_datetime ,quantity ,unit_of_quantity ,destination_number ,serving_cell_address ,gdr_id ,call_type ,extbillingaccountid ,cdate ,etl_date))



connection = connect()
create_tables(connection)

import pandas as pd

data = pd.read_excel("dwa_police_report_20180924.xlsx")


for i in range(len(data)-1):
    b= data.iloc[i+1:i+2,0:].values.tolist()
    for j in b:
        listem = list()
        for x in j:
            print(x,'**')
            listem.append(str(x))
        add_sensorlog(connection,listem[0],listem[1],listem[2],listem[3],listem[4],listem[5],listem[6],listem[7],
                         listem[8],listem[9],listem[10],listem[11],listem[12],listem[13],listem[14],listem[15],
                         listem[16],listem[17],listem[18], listem[19],listem[20],listem[21],
                         listem[22],listem[23],listem[24],listem[25],listem[26],listem[27])


connection.close()

