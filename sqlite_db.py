import sqlite3
from sqlite3 import Error
import pandas as pd

DATABASE_NAME = "sample_sqlite.db"

def create_connection():
    """ Create or connect to an SQLite database """
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except Error as e:
        print(e)
    return conn

def query_database(query):
    """ Run SQL query and return results in a dataframe """
    conn = create_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_schema_representation(table_name):
    """ Get the database schema in a JSON-like format """
    conn = create_connection()
    cursor = conn.cursor()

    db_schema = {}


    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()

    column_details = {}
    for column in columns:
        column_name = column[1]
        column_type = column[2]
        column_details[column_name] = column_type

    db_schema[table_name] = column_details

    conn.close()
    return db_schema

def query_database_for_tables(query):
    """ Run SQL query and return results in a dataframe """
    conn = create_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df['name'].tolist()
