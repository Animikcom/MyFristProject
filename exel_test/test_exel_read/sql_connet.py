import pyodbc
from datetime import datetime, timedelta
import pandas as pd



cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=WIN-IVTEF69OMJ5\ANIMIKSERVER;"
            "Database=Real EstateSQL;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)


cursor = cnxn.cursor()
data = cursor.execute("SELECT TOP(100) * FROM tblOwners")

meta = data.fetchall()
print(meta)
# data = pd.read_sql("SELECT TOP(100) * FROM associates", cnxn)