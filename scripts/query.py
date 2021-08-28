import sqlite3
from sqlite3 import Error
import pandas as pd
import sys, getopt

def connection_DB():
    conn = sqlite3.connect("db_files/cancer_data.db")
    cur = conn.cursor()
    return conn,cur

def create_table(table_name):
       
    create_query = " CREATE TABLE IF NOT EXISTS "+table_name+""" (
    radius_mean FLOAT DEFAULT NULL,
    perimeter_mean FLOAT DEFAULT NULL,
    area_mean FLOAT DEFAULT NULL, 
    concavity_mean FLOAT DEFAULT NULL,
    'concave points_mean' FLOAT DEFAULT NULL,
    area_se FLOAT DEFAULT NULL,
    radius_worst FLOAT DEFAULT NULL,
    perimeter_worst FLOAT DEFAULT NULL,
    area_worst FLOAT DEFAULT NULL, 
    'concave points_worst' FLOAT DEFAULT NULL,
    diagnosis FLOAT DEFAULT NULL)""" 
    conn, cur = connection_DB()
    cur.execute(create_query)
    conn.commit() 
    cur.close()

def insert_data(df: pd.DataFrame,table_name):
    conn, cur = connection_DB()
    for _,row in df.iterrows():
        insert_query = "INSERT INTO "+ table_name + """(radius_mean,perimeter_mean,area_mean, 
                                            concavity_mean,'concave points_mean',area_se,radius_worst,
                                            perimeter_worst,area_worst,'concave points_worst',diagnosis )values(?,?,?,?,?,?,?,?,?,?,?)"""
        to_be_inserted = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])

        cur.execute(insert_query,to_be_inserted)
        conn.commit() 
    cur.close()

def fetch_data(table_name):
    conn, cur = connection_DB()
    colmn_names = []
    select_query = "select * FROM "+table_name
    values =cur.execute(select_query)
    for desc in cur.description:
        colmn_names.append(desc[0])

    conn.commit()
    df = pd.DataFrame(values, columns=colmn_names)
    cur.close()
    return df


if __name__ == '__main__':
    create_table("cleaned_cancer_data")
    df = pd.read_csv("data/data.csv")
    insert_data(df,"cleaned_cancer_data")
    print(fetch_data("cleaned_cancer_data"))

    