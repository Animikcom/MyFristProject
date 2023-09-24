# import pymssql
import pandas as pd

con = mssql.connect('Real EstateSQL.db')
wb = pd.read_excel('tblAccount.xlsx', engine='openpyxl', sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()