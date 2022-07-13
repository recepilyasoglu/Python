import psycopg2
import os
import sqlite3


def connect(conn):
    return sqlite3.connect("ddl.db")

def copy_from_file(conn, data, table):
    """
    Here we are going save the dataframe on disk as 
    a csv file, load the csv file  
    and use copy_from() to copy it to the table
    """
    # Save the dataframe to disk
    tmp_data = "dwa_police_report_20180924.csv"
    data.to_csv(tmp_data, index_label='id', header=False)
    f = open(tmp_data, 'r')
    cursor = conn.cursor()
    try:
        cursor.copy_from(f, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        os.remove(tmp_data)
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_file() done")
    cursor.close()
    os.remove(tmp_data)
    
    conn = connect() # connect to the database
    copy_from_file(conn, 'dwa_police_report_20180924.csv', 'recep') # copy the dataframe to SQL
    conn.close() # close the connection
    
