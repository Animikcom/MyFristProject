import pyodbc as odbccon

conn = odbccon.connect("Driver={SQL Server Native Client 11.0};"
                       "Server=WIN-IVTEF69OMJ5\ANIMIKSERVER;"
                       "Database=Real EstateSQL;"
                       "Trusted_Connection=yes;"
                       )
cursor = conn.cursor()
cursor.execute('Select * from tblBuilding')
for row in cursor:
    print('row = %r' %(row,))