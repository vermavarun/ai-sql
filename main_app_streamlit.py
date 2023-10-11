import streamlit as st
import pandas as pd
import ms_sql_db
from prompts.prompts import SYSTEM_MESSAGE
from azure_openai import get_completion_from_messages
import json
import os
import sqlite_db

def query_database(query, conn):
    """ Run SQL query and return results in a dataframe """
    return pd.read_sql_query(query, conn)

st.title("SQL Query Generator with GPT-4")

db_type = st.selectbox(
     'Which DB do you want to query?',
     ('SQLite','MS-SQL'))
db_type = db_type or 'SQLite'
st.write('You selected:', db_type)


table_name = st.selectbox(
     'Which table do you want to query?',
     ('students','finance'))
table_name = table_name or 'students'
st.write('You selected:', table_name)

user_message = st.text_input("Enter your message to generate SQL and view results:")

if user_message:
    if db_type =="MS-SQL":
        conn = ms_sql_db.create_connection()
        schemas = ms_sql_db.get_schema_representation(table_name)
    if db_type =="SQLite":
        conn = sqlite_db.create_connection()
        schemas = sqlite_db.get_schema_representation(table_name)
    # Format the system message with the schema
    formatted_system_message = SYSTEM_MESSAGE.format(schema=schemas[table_name],table_name=table_name)

    # Use GPT-4 to generate the SQL query
    response = get_completion_from_messages(formatted_system_message, user_message,os.getenv("AZURE_DEPLOYMENT_NAME"))
    json_response = json.loads(response)
    query = json_response['query']

    # Display the generated SQL query
    st.write("Generated SQL Query:")
    st.code(query, language="sql")

    try:
        # Run the SQL query and display the results
        sql_results =  query_database(query, conn)
        st.write("Query Results:")
        st.dataframe(sql_results)
        st.area_chart(sql_results)

    except Exception as e:
        st.write(f"An error occurred: {e}")
