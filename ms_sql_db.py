import pandas as pd
import pyodbc
import os

#print(pyodbc.drivers())

def create_connection():
    """ Create or connect to an SQLite database """
    conn = None;
    try:
        ms_mql_db_name=os.getenv("MS_SQL_DB_NAME")
        ms_mql_server_name=os.getenv("MS_SQL_SERVER_NAME")
        ms_mql_uid=os.getenv("MS_SQL_UI")
        ms_mql_pwd=os.getenv("MS_SQL_PWD")
        ms_mql_driver_name=os.getenv("MS_SQL_DRIVER")

        conn = pyodbc.connect('Driver='+ms_mql_driver_name+';'
                        'Server='+ms_mql_server_name+';'
                        'Database='+ms_mql_db_name+';'
                        'uid='+ms_mql_uid+';'
                        'pwd='+ms_mql_pwd+';')
    except Exception as e:
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

    # Query to get column details for each table
    cursor.execute(f"select COLUMN_NAME, DATA_TYPE from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{table_name}'")
    columns = cursor.fetchall()
    db_schema = {}
    column_details = {}
    for column in columns:
        column_name = column[0]
        column_type = column[1]
        column_details[column_name] = column_type

    db_schema[table_name] = column_details

    conn.close()
    return db_schema

def query_database_for_tables(query):
    conn = create_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df['TABLE_NAME'].tolist()
