Text To SQL with MS SQL Server Connectivity

`streamlit run .\main_app_streamlit.py`

To run the MS-SQL

    docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=yourStrong(!)Password" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest