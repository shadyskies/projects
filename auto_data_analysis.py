import matplotlib.pyplot as pyt
import mysql.connector
import pandas as pd #for read_excel: xlrd and openpyxl
from pandas.api.types import is_numeric_dtype, is_float_dtype
import numpy as np
import os
from sqlalchemy import create_engine 


def get_source(file):
    if not os.path.exists(file):
        print("File does not exist")
        return

    idx = file.rfind(".")
    extension = file[idx+1:]
    
    if extension == "csv":
        extract_csv(file)
    if extension == "xlsx":
        extract_xl(file)

#TODO: implement outlier detection and align cols
def extract_csv(file):
    df = pd.read_csv(file)
    print(f"Rows:{df.shape[0]} Columns:{df.shape[1]}")
    # print(df.head())
    cols = df.columns
    print(f"Column\t\t Mean\t\t\tMedian\t\t\tNullVals")
    for i in range(len(cols)):
        if is_numeric_dtype(df[cols[i]]) or is_float_dtype(df[cols[i]]):
            print(f"{cols[i]}\t {round(df[cols[i]].mean(),3)}\t {round(df[cols[i]].median(),3)}\t {df[cols[i]].isna().sum()}")
    return df

def extract_xl(file):
    df = pd.read_excel('boston_house.xlsx', sheet_name=0)
    print(f"")
    # print(df.head())
    cols = df.columns
    print(f"Column\t\t Mean\t\t\tMedian\t\t\tNullVals")
    for i in range(len(cols)):
        if is_numeric_dtype(df[cols[i]]) or is_float_dtype(df[cols[i]]):
            print(f"{cols[i]}\t {round(df[cols[i]].mean(),3)}\t {round(df[cols[i]].median(),3)}\t {df[cols[i]].isna().sum()}")
    return df

def plots():
    val = input("Enter type of plot: ")



def get_from_db():
    tmp = input("Enter user, password and database to access: ").split()
    if len(tmp)!=3:
        print("Too many or too less arguments! Exiting...")
        return
    # print("Connecting and extracting from db...")
    print(tmp)
    mydb = mysql.connector.connect(
        host="localhost",
        user="django_projects",
        password="django_projects_pwd",
        database="emp"
    )
    db_connection_url = f"mysql://django_projects:django_projects_pwd@localhost/emp"
    db_connection = create_engine(db_connection_url)

    df = pd.read_sql("SELECT * FROM EMPLOYEE", con=db_connection)
    print(df.head)
    #print cols
    print(df.columns.ravel)
    return df


if __name__ == "__main__":
    val = int(input("Enter 0 to select from database or 1 to select file..."))
    if (val == 1):
        file = input("Enter file name...")
        get_source(file)
    else:
        get_from_db()